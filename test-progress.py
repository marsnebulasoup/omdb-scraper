import time
import dbm
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn



tasks = [f'tt00{i}' for i in range(1000, 1100)]

def do_work(task):
    time.sleep(0.1)
    return task

with Progress(
        SpinnerColumn(),
        MofNCompleteColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
    ) as db_progress:
        db_progress_bar = db_progress.add_task("Loading DB...", total=None)
        db = dbm.open("omdb_data", "w")
        db_progress.update(db_progress_bar, description="DB loaded")
        db_progress.stop_task(db_progress_bar)
        db.close()