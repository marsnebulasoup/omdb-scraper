import ijson

DEFAULT_UNKNOWN_VALUE = "N/A"
KEYS = [
    "Title",
    "Year",
    "Rated",
    "Released",
    "Runtime",
    "Genre",
    "Director",
    "Writer",
    "Actors",
    "Plot",
    "Language",
    "Country",
    "Awards",
    "Poster",
    "Tomatometer",
    "Metascore",
    "imdbRating",
    "imdbVotes",
    "imdbID",
    "Type",
    "DVD",
    "BoxOffice",
    "Production",
    "Website",
    "Response",
    "totalSeasons",
    "Season",
    "Episode",
    "seriesID",
]

# the Tomatometer key is not in the original JSON; this pulls it from the ratings array
def get_tomatometer(entry):
    if "Ratings" in entry:
        for rating in entry["Ratings"]:
            if rating["Source"] == "Rotten Tomatoes":
                return rating["Value"]
    return DEFAULT_UNKNOWN_VALUE


def escape_quotes(item):
    # to escape quotes in csv files you need to precede them with another quote
    return item.replace('"', '""')


def join_line(entry):
    return ",".join(f'"{escape_quotes(item)}"' for item in entry) + "\n"

def get_line(entry):
  for key in KEYS:
      value = DEFAULT_UNKNOWN_VALUE
      
      if key in entry:
          value = entry[key]
      elif key == "Tomatometer":
          value = get_tomatometer(entry)
      
      yield value

def write_csv(db_name, progress, progress_bar):
  progress.log("Writing JSON to CSV...")
  progress.start_task(progress_bar)
  
  json = open(f"{db_name}.json", "r", encoding="utf-8")
  csv = open(f"{db_name}.csv", "w", encoding="utf-8")

  data = ijson.items(json, "item")

  csv.write(join_line(KEYS))  # write header

  for entry in data:
      line = join_line(get_line(entry))
      csv.write(line)
      progress.update(progress_bar, advance=1)

  json.close()     
  csv.close()

  progress.log("JSON written to CSV.")
