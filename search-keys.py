import dbm
import rich

DB = dbm.open("omdb_data", "r")

repeat = 'y'
while repeat == 'y':
    key = input("Key: ")
    try: 
      data = str(DB.get(key), "utf-8")
      with open(f"{key}.json", "w") as f:
        f.write(data)
      rich.print_json(data)
    except:
      print("Key not found")

    print("\n")