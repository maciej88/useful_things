import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"
# print(sys.argv[1:])

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# save_items("testitem.json", {"key": "value"})
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    # print(command)

    if command == "save":
        # print("save")
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("please type exactly one command")