# Update
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)

# Insert
myList = [1,2,3,4,5,6,7]
newList = [11,23,13,14]
print(myList)
myList.insert(4, 11) # Anywhere in list; at index 0 insert 11
print(myList)
myList.append(55) # Only at the end of list
print(myList)
myList.extend(newList) # Adds new list to existing list
print(myList)
