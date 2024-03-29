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
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    elif command == "delete":
        key = input("Enter a key: ")
        if key in data:
            data.pop(key[, default])
            # del data[key]
            print("Key delete")
    else:
        print("Unknown command")
else:
    print("please type exactly one command")