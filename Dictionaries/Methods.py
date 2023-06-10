# Dictionary Methods


# copy() - returns shallow copy of dict
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
dict = myDict.copy()
print(dict)

# fromkeys()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
newDict = {}.fromkeys([1,2,3],0)
print(newDict)

# get()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.get('example'))

# items()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.items())

# keys()
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}
print(myDict.keys())
