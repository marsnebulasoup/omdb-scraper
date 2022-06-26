import simplejson as json


def get_entries(db, progress, progress_bar):
    for key in db.keys():
        try:
            raw_data = db[key].decode("utf-8", "backslashreplace")
            json_data = json.loads(raw_data)
        except:
            key_str = str(key, "utf-8")
            progress.log(f"Error converting {key_str}")

            # If you manually fix the bad entries, placing each one into a separate file, you can uncomment these to load them
            # with open(f"fixed/{k}.json", "r", encoding="utf-8") as f:
            #   json_data = json.load(f)
            #   yield json_data
        else:
            if json_data["Response"] == "True":
                yield json_data

        progress.update(progress_bar, advance=1)


def write_json(db, db_name, progress, progress_bar):
    progress.log("Writing DB to JSON...")
    progress.start_task(progress_bar)

    json_file = open(f"{db_name}.json", "w")
    json.dump(
        get_entries(db, progress, progress_bar), json_file, iterable_as_array=True
    )
    json_file.close()

    progress.log("DB written to JSON.")
