try:
    from rich.progress import (
        Progress,
        SpinnerColumn,
        TimeElapsedColumn,
        MofNCompleteColumn,
    )
    import asyncio
    import aiohttp
    import dbm
    import json
    from dotenv import dotenv_values
    from create_db import create_db
    from write_json import write_json
    from write_csv import write_csv
except:
    print("Error importing modules. Please install the required modules.")
    exit()

try:
    API_KEY = dotenv_values(".env")["API_KEY"]
except:
    print(
        "Error loading API key. Please make sure you have a .env file with the API key under 'API_KEY'."
    )
    exit()

ID_PATH = "title.ratings.tsv/data.tsv"
DB = "db/omdb_data"
MAX_CONCURRENT_TASKS = 50
RETRY_COUNT = 3
URL = f"http://www.omdbapi.com/?apikey={API_KEY}&i="

PROGRESS = Progress(
    SpinnerColumn(),
    MofNCompleteColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
)
PROG_BAR_DB = PROGRESS.add_task("Loading DB", start=True, total=None)
PROG_BAR_READ = PROGRESS.add_task("Reading DB", start=False)
PROG_BAR_REQ = PROGRESS.add_task("Making Requests", start=False)
PROG_BAR_WRITING_JSON = PROGRESS.add_task("Writing DB to JSON", start=False)
PROG_BAR_WRITING_CSV = PROGRESS.add_task("Converting JSON to CSV", start=False)

FAILED_ENTRIES = 0


def save(db, key, data):
    db[key] = data


def verify_entry(entry):
    resp = "False"

    try:
        resp = json.loads(entry)["Response"]
    except:
        pass

    return resp == "True"


async def fetch(key, session, count=0):
    url = f'{URL}{str(key, "utf-8")}'
    async with session.get(url) as response:
        data = False
        if response.status == 200:
            text = await response.text()
            if verify_entry(text):
                data = text
            elif count < RETRY_COUNT:
                data = await fetch(key, session, count + 1)
        elif count < RETRY_COUNT:
            data = await fetch(key, session, count + 1)
        return data


async def fetch_and_save(sem, session, key, db):
    global FAILED_ENTRIES
    async with sem:
        data = await fetch(key, session)
        if data:
            save(db, key, data)
        else:
            FAILED_ENTRIES += 1
        PROGRESS.update(PROG_BAR_REQ, advance=1)
        return data


async def concurrent_scheduler(db):
    sem = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

    async with aiohttp.ClientSession() as session:
        PROGRESS.log("Reading DB; looking for empty entries...")
        PROGRESS.start_task(PROG_BAR_READ)

        tasks = []
        completed_entries = 0
        for key in db.keys():
            if verify_entry(db[key]):
                completed_entries += 1
            else:  # not yet fetched or bad data
                tasks.append(asyncio.create_task(fetch_and_save(sem, session, key, db)))

            PROGRESS.update(PROG_BAR_READ, advance=1)

        PROGRESS.log(f"Found {len(db) - completed_entries} empty entries.")
        PROGRESS.log(f"Filled entries: {completed_entries}/{len(db)}")
        PROGRESS.log(f"Fetching remaining {len(db) - completed_entries} entries...")
        PROGRESS.update(PROG_BAR_REQ, advance=completed_entries)
        PROGRESS.start_task(PROG_BAR_REQ)

        await asyncio.gather(*tasks)


def load_db():
    PROGRESS.log("Loading DB...")
    db = False
    try:
        db = dbm.open(DB, "w")
    except:
        PROGRESS.log(f"DB '{DB}' not found.")
    else:
        PROGRESS.update(PROG_BAR_DB, description="DB loaded", total=100, advance=100)
        PROGRESS.log("DB loaded.")
    finally:        
        PROGRESS.stop_task(PROG_BAR_DB)

    return db


if __name__ == "__main__":
    PROGRESS.__enter__()
    PROGRESS.log("\n>>>>> STARTING <<<<<\n")
    
    db = load_db()
    if not db:
        db = create_db(ID_PATH, DB, PROGRESS, PROG_BAR_DB)

    PROGRESS.update(PROG_BAR_READ, total=len(db))
    PROGRESS.update(PROG_BAR_REQ, total=len(db))
    PROGRESS.update(PROG_BAR_WRITING_JSON, total=len(db))
    PROGRESS.update(PROG_BAR_WRITING_CSV, total=len(db))

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(concurrent_scheduler(db))

    PROGRESS.log("Completed.")
    if FAILED_ENTRIES:
      PROGRESS.log(
          f"Failed to fetch {FAILED_ENTRIES}/{len(db)} entries - rerun to try again."
      )
    else:
      PROGRESS.log("All entries fetched successfully.")

    write_json(db, DB, PROGRESS, PROG_BAR_WRITING_JSON)
    write_csv(DB, PROGRESS, PROG_BAR_WRITING_CSV)

    db.close()

    PROGRESS.log("\n>>>>> FINISHED <<<<<\n")
    PROGRESS.__exit__(None, None, None)
