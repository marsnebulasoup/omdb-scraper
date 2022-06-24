import json
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, MofNCompleteColumn

# data = [
#     {
#         "Title": "Carmencita",
#         "Year": "1894",
#         "Rated": "Not Rated",
#         "Released": "10 Mar 1894",
#         "Runtime": "1 min",
#         "Genre": "Documentary, Short",
#         "Director": "William K.L. Dickson",
#         "Writer": "N/A",
#         "Actors": "Carmencita",
#         "Plot": "Performing on what looks like a small wooden stage, wearing a dress with a hoop skirt and white high-heeled pumps, Carmencita does a dance with kicks and twirls, a smile always on her face.",
#         "Language": "None",
#         "Country": "United States",
#         "Awards": "N/A",
#         "Poster": "https://m.media-amazon.com/images/M/MV5BZmUzOWFiNDAtNGRmZi00NTIxLWJiMTUtYzhkZGRlNzg1ZjFmXkEyXkFqcGdeQXVyNDE5MTU2MDE@._V1_SX300.jpg",
#         "Ratings": [{"Source": "Internet Movie Database", "Value": "5.7/10"}],
#         "Metascore": "N/A",
#         "imdbRating": "5.7",
#         "imdbVotes": "1,888",
#         "imdbID": "tt0000001",
#         "Type": "movie",
#         "DVD": "N/A",
#         "BoxOffice": "N/A",
#         "Production": "N/A",
#         "Website": "N/A",
#         "Response": "True",
#     },
#     {
#         "Title": "Le clown et ses chiens",
#         "Year": "1892",
#         "Rated": "N/A",
#         "Released": "28 Oct 1892",
#         "Runtime": "5 min",
#         "Genre": "Animation, Short",
#         "Director": "\u00c9mile Reynaud",
#         "Writer": "N/A",
#         "Actors": "N/A",
#         "Plot": "Short film of 300 individually painted images.",
#         "Language": "None",
#         "Country": "France",
#         "Awards": "N/A",
#         "Poster": "https://m.media-amazon.com/images/M/MV5BZDI4ZDgwMWQtMjA3ZS00NmU5LTk5MGQtZTMyMGFlMjYyZmFlXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX300.jpg",
#         "Ratings": [{"Source": "Internet Movie Database", "Value": "6.0/10"}],
#         "Metascore": "N/A",
#         "imdbRating": "6.0",
#         "imdbVotes": "250",
#         "imdbID": "tt0000002",
#         "Type": "movie",
#         "DVD": "N/A",
#         "BoxOffice": "N/A",
#         "Production": "N/A",
#         "Website": "N/A",
#         "Response": "True",
#     },
#     {
#         "Title": "Pauvre Pierrot",
#         "Year": "1892",
#         "Rated": "TV-PG",
#         "Released": "28 Oct 1892",
#         "Runtime": "4 min",
#         "Genre": "Animation, Comedy, Short",
#         "Director": "\u00c9mile Reynaud",
#         "Writer": "N/A",
#         "Actors": "N/A",
#         "Plot": "One night, Arlequin come to see his lover Colombine. But then Pierrot knocks at the door and Colombine and Arlequin hide. Pierrot starts singing but Arlequin scares him and the poor man goes away.",
#         "Language": "None",
#         "Country": "France",
#         "Awards": "N/A",
#         "Poster": "https://m.media-amazon.com/images/M/MV5BYWZiY2U3MjgtMzYzNS00OGUzLWI3OTQtNjkyMmZiZjEzNDc2XkEyXkFqcGdeQXVyOTUzMjk0NDE@._V1_SX300.jpg",
#         "Ratings": [{"Source": "Internet Movie Database", "Value": "6.5/10"}],
#         "Metascore": "N/A",
#         "imdbRating": "6.5",
#         "imdbVotes": "1,666",
#         "imdbID": "tt0000003",
#         "Type": "movie",
#         "DVD": "N/A",
#         "BoxOffice": "N/A",
#         "Production": "N/A",
#         "Website": "N/A",
#         "Response": "True",
#     },
# ]


with open("omdb_data.json", "r") as f:
    data = json.load(f)

keys = []


def get_keys(data, update_progress=None):
    if type(data) is list:
        for item in data:
            get_keys(item)
            if update_progress:
                update_progress()
    elif type(data) is dict:
        for key in data.keys():
            if key not in keys:
                keys.append(key)
                get_keys(data[key])


with Progress(
    SpinnerColumn(),
    MofNCompleteColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
) as progress:
    db_progress_bar = progress.add_task("Searching", total=len(data))
    update_progress = lambda: progress.update(db_progress_bar, advance=1)
    get_keys(data, update_progress)
    print(keys)
    for key in keys: print(key)
