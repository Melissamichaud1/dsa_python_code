# Slice[:]
print('Slice')
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2]) # Does not include 2nd index
print(myList[:2]) # 0 can be omitted
print(myList[1:]) # Starts at index 1 and prints all elements to the right
myList[0:2] = ['x','y'] # Update multiple elements
print(myList)

# Delete
myList = ['a', 'b', 'c', 'd', 'e', 'f']
# Pop
print('Pop')
myList.pop(1) # Pop() removes index 1
myList.pop() # Deletes last element
print(myList)

# Delete
print('Delete')
myListTwo = ['a', 'b', 'c', 'd', 'e', 'f']
del myListTwo[1] # Deletes index 1
del myListTwo[0:2] # Deletes first 2 indexes
print(myListTwo)

# Remove
print('Remove')
myListThree = ['a', 'b', 'c', 'd', 'e', 'f']
myListThree.remove('e')
print(myListThree)
