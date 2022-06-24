import dbm
import json
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn

empty = 0
total = 0
DB = dbm.open("omdb_data", "r")

with Progress(
        SpinnerColumn(),
        MofNCompleteColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
    ) as progress:        
        db_progress_bar = progress.add_task("Searching", total=len(DB))   
        for key in DB.keys():
          try:
            resp = json.loads(DB[key])["Response"]
          
            if resp == "False":
              empty+=1
              # progress.log(f"{key} is empty")
          except:
            progress.log(f"{key} is bad")
            pass
          total+=1
          progress.update(db_progress_bar, advance=1)
        progress.log(f"Empty: {empty}/{total} or {empty/total*100}%")
DB.close()