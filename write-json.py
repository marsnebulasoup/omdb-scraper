import dbm
import json
from json.decoder import JSONDecodeError
import re
import traceback
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn

DB = dbm.open("omdb_data", "w")

data = []

# class LazyDecoder(json.JSONDecoder):
#     def decode(self, s, **kwargs):
#         regex_replacements = [
#             (re.compile(r'\\'), r'\\\\'),
#         ]
#         for regex, replacement in regex_replacements:
#             s = regex.sub(replacement, s)
#         return super().decode(s, **kwargs)


def permissive_json_loads(text):
    while True:
        try:
            data = json.loads(text)
        except JSONDecodeError as exc:
            if exc.msg == 'Invalid \\escape':
                text = text[:exc.pos] + '\\' + text[exc.pos:]
            else:
                raise
        else:
            return data

with Progress(
        SpinnerColumn(),
        MofNCompleteColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
    ) as progress:
        progress.log("Loading DB...")
        

        db_progress_bar = progress.add_task("Converting to JSON", total=len(DB))   

        for key in DB.keys():
            try:
              s_data = DB[key].decode("utf-8", "backslashreplace")
              j_data = json.loads(s_data)
            except:
              k = str(key, "utf-8")
              progress.log(f"Error converting {k}")
  
              with open(f"fixed/{k}.json", "r", encoding="utf-8") as f:
                j_data = json.load(f)
                data.append(j_data)
       
            else:
              if j_data["Response"] == "True":
                data.append(j_data)
            progress.update(db_progress_bar, advance=1)

        with open("omdb_data.json", "w") as f:
            json.dump(data, f, indent=2)

DB.close()