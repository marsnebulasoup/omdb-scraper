import json
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn

DEFAULT_UNKNOWN_VALUE = "N/A"

with open("omdb_data.json", "r") as f:
    data = json.load(f)


def getTomatometer(entry):
    if "Ratings" in entry:
        for rating in entry["Ratings"]:
            if rating["Source"] == "Rotten Tomatoes":
                return rating["Value"]
    return DEFAULT_UNKNOWN_VALUE


def escapeQuotes(item):
    # to escape quotes in csv files you need to precede them with another quote
    return item.replace('"', '""')


keys = [
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

csv = open("omdb_data.csv", "w", encoding="utf-8")

with Progress(
    SpinnerColumn(),
    MofNCompleteColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
) as progress:
    db_progress_bar = progress.add_task("Writing", total=len(data))
    update_progress = lambda: progress.update(db_progress_bar, advance=1)

    csv.write(
        ",".join(f'"{escapeQuotes(item)}"' for item in keys) + "\n"
    )  # write header

    # count = 0

    for entry in data:
        line = []
        for key in keys:
            value = DEFAULT_UNKNOWN_VALUE
            if key in entry:
                value = entry[key]
            elif key == "Tomatometer":
                value = getTomatometer(entry)
            line.append(value)
        csv.write(",".join(f'"{escapeQuotes(item)}"' for item in line) + "\n")
        update_progress()

        # count += 1
        # if count == 100:
        #     break


csv.close()
