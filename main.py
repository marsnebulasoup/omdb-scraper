from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn
import asyncio
import aiohttp
import time
import dbm
import json
from dotenv import dotenv_values

API_KEY = dotenv_values(".env")["API_KEY"]

db = "omdb_data"

MAX_CONCURRENT_TASKS = 50
RETRY_COUNT = 3
MAX_REQUESTS = len(db)
URL = f"http://www.omdbapi.com/?apikey={API_KEY}&i="

BAD_KEYS = []

def save(db, key, data):
    db[key] = data


def verify_entry(entry):
    resp = "False"

    try:
        resp = json.loads(entry)["Response"]
    except:
        pass

    return resp == "True"


async def fetch(url, session, count=0):
    async with session.get(url) as response:
        data = False
        if response.status == 200:
            text = await response.text()
            if verify_entry(text):
                data = text
            elif count < RETRY_COUNT:
                time.sleep(0.05)
                data = await fetch(url, session, count + 1)
        elif count < RETRY_COUNT:
            time.sleep(0.05)
            data = await fetch(url, session, count + 1)
        return data


async def bound_fetch(sem, url, session, key, db, progress, update_progress):
    # Getter function with semaphore.
    async with sem:
        data = await fetch(url, session)
        if data:
            save(db, key, data)
        else:
            # progress.log(f"Error fetching key {key}")
            BAD_KEYS.append(key)
        update_progress()
        return data


async def concurrent_scheduler(
    progress,
    task_loader_progress_bar,
    requests_progress_bar,
    update_task_loader_progress,
    update_request_progress,
    db,
):
    # use aiohttp
    sem = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

    async with aiohttp.ClientSession() as session:
        tasks = []
        skipped = 0
        progress.log("Loading tasks...")
        for key in db.keys():
            if verify_entry(db[key]):
                skipped += 1
            else:  # not yet fetched or bad data
                url = f'{URL}{str(key, "utf-8")}'
                tasks.append(
                    asyncio.create_task(
                        bound_fetch(
                            sem,
                            url,
                            session,
                            key,
                            db,
                            progress,
                            update_request_progress,
                        )
                    )
                )

            update_task_loader_progress()

        progress.log("Running tasks...")
        progress.log(f"Skipping {skipped} tasks...")
        progress.update(requests_progress_bar, advance=skipped)
        progress.start_task(requests_progress_bar)
        # exit()
        await asyncio.gather(*tasks)


if __name__ == "__main__":

    with Progress(
        SpinnerColumn(),
        MofNCompleteColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
    ) as progress:
        progress.log("Loading DB...")
        db_progress_bar = progress.add_task("Loading DB...", start=True, total=None)
        db = dbm.open("omdb_data", "w")
        progress.update(
            db_progress_bar, description="DB loaded", total=100, advance=100
        )
        progress.log("DB loaded")

        task_loader_progress_bar = progress.add_task("Loading Tasks", total=len(db))
        requests_progress_bar = progress.add_task(
            "Making Requests", total=len(db), start=False
        )
        update_task_loader_progress = lambda: progress.update(
            task_loader_progress_bar, advance=1
        )
        update_request_progress = lambda: progress.update(
            requests_progress_bar, advance=1
        )

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(
            concurrent_scheduler(
                progress,
                task_loader_progress_bar,
                requests_progress_bar,
                update_task_loader_progress,
                update_request_progress,
                db,
            )
        )

        with open("bad_keys.txt", "w") as f:
            for key in BAD_KEYS:
                f.write(str(key) + "\n")

        db.close()
