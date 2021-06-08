import json
manager = {'name': 'Kevin Ejele', 'school': ['unn', 'fgc', 'lea']}
director = {'name': 'Justice David', 'school': ['Debrecen', 'fgc', 'Sokoga']}

staff = {'senior': manager, 'junior': director}

# adding a items to a nested dict *** an item can be added by first creating the object or added directly as shown below

# boss = {'name': 'Guchi', 'school': ['Haverd', 'unn', 'rockland']}

# adding items to the staff
staff['member'] = boss = [
    {'name': 'Guchi', 'school': ['Haverd', 'unn', 'rockland']}]

# prints out all of the staff dict
print(staff)
print()

# printing out the first item of school list in junior key
print(staff['junior']['school'][0])
print()

# printing out the first item(name) from the boss list of dict
print(staff['member'][0]['name'])
print()


# converting file(dictionary) to json
staff_file = json.dumps(staff)
print(staff_file)
