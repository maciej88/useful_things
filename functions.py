def build_person(first_name, last_name):
    full_name = f"imię: {first_name.title()} nazwisko: {last_name.title()}"
    return full_name

name = input('podaj imie: ')
surname = input('podaj nazwisko: ')

print(build_person(name, surname))