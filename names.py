from name_function import get_formatted_name

print("type q for exit")
while True:
    first = input("\nPodaj imię: ")
    if first == 'q':
        break
    last = input("Podaj nazwisko: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tSformatowane: {formatted_name}")