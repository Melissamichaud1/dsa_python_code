# Question 5 - Is Unique: Implement an algorithm to determine if a list has all unique characters, using python list

myList = [1,20,30,44,5,56,57,8,10,31,12,19,13,14,35,16,27,58,19,21]

def isUnique(lst):
    newList = []
    for num in lst:
        if num in newList:
            print(num)
            return False
        else:
            newList.append(num)
    return True

print(isUnique(myList))
