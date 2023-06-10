# Searching -- IN operator and Linear search

# IN
myList = [10,20,30,40,50,60,70,80,90]
if 20 in myList:
    print(myList.index(20))
else:
    print('The value does not exist in the list')


# Linear search = checks each element in list
myListTwo = [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myListTwo, 20))
