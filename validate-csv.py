import csv
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn

FILENAME = "omdb_data.csv"


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


with Progress(
    SpinnerColumn(),
    MofNCompleteColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
) as progress:

    with open(FILENAME, encoding="utf-8") as csvfile:
        db_progress_bar = progress.add_task("Reading", total=get_line_count(FILENAME))
        update_progress = lambda: progress.update(db_progress_bar, advance=1)
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        count = 0
        for row in reader:
            if count % 10000 == 0:
              progress.log(f'{row}')
            count+=1
            update_progress()
