from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
import dbm


def get_line_count(fname):
    def _make_gen(reader):
        while True:
            b = reader(2**16)
            if not b:
                break
            yield b

    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
    return count


def create_db(id_path, db_name, progress, progress_bar):
    progress.update(progress_bar, description="Creating DB")
    progress.log("Creating DB...")
    progress.log("Loading ID file...")
    try:
      line_count = get_line_count(id_path)
      id_file = open(id_path, "r")
    except FileNotFoundError:
      progress.log(f"Error: ID file not found at {id_path}")
      exit()
    else:
      progress.log("ID file loaded.")

    db = dbm.open(db_name, "c")

    progress.update(progress_bar, total=line_count)

    line = id_file.readline()
    line = id_file.readline()  # skip header

    while line:
        line = line.split("\t")
        imdbID = line[0]
        db[imdbID] = '{"Response": "Empty"}'

        line = id_file.readline()
        progress.update(progress_bar, advance=1)

    id_file.close()
    progress.update(progress_bar, description="DB created")
    progress.log("DB created.")
    return db
