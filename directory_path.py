import os

#get current directory
path = os.getcwd()
print(f"Current directory: {path}")
print("===============================================================")
#get parent directory
parent = os.path.dirname(path)
print(f"Parent directory {parent}")

