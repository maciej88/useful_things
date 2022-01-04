name = "jan kowalski"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "jan"
last_name = 'kowalski'
full_name1 = first_name + " " + last_name
full_name2 = f"{first_name} versus {last_name.title()}"
print(full_name1)
print(full_name2)

print("python")
print("\tPython")
print("python")
print("\nPython\nPython")
print("\n\tPython\nPython")

favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
# usuwa biały znak z prawej; x.lstrip() z lewej a x.strip() z obu
