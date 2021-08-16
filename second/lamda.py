
# without lambda function

def sorter(item: str) -> str:
    return item['age']


millioniares = [{'name': 'Kevin Ejele', 'school': 'unn', 'age': 31}, {
    'name': 'Justice David', 'school': 'Debrecen', 'age': 36}]


millioniares.sort(key=sorter)

print(millioniares)


# with lambda

millioniares.sort(key=lambda item: len(['school']))

print()
print(millioniares)
