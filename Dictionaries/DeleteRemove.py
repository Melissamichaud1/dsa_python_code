# Delete an element from a dictionary

# pop()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.pop('name'))
print(myDict)


# popitem()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.popitem())
print(myDict)


# clear()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
myDict.clear()
print(myDict)


# del keyword
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
del myDict['age']
print(myDict)
