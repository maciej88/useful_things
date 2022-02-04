def build_person(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musican = build_person('jimi', 'hendrix')
print(musican)