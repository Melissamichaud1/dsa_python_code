# Traversing through a dictionary

myDict = {'name': 'Edy', 'age':26, 'address':'london'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

# Searching - finding an element

myDict = {'name': 'Edy', 'age':26, 'address':'london'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

print(searchDict(myDict, 26))
