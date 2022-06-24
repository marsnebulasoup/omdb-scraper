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


line_count = get_line_count("title.ratings.tsv/data.tsv")

id_file = open("title.ratings.tsv/data.tsv", "r")
db = dbm.open('omdb_data', 'c')

with Progress(
    SpinnerColumn(), *Progress.get_default_columns(), TimeElapsedColumn()
) as progress:

    db_progress = progress.add_task("Setting Keys", total=line_count)

    line = id_file.readline()
    line = id_file.readline() # skip header
    
    while line:
        line = line.split("\t")
        imdbID = line[0]
        db[imdbID] = '0'
      
        line = id_file.readline()
        progress.update(db_progress, advance=1)

db.close()
id_file.close()