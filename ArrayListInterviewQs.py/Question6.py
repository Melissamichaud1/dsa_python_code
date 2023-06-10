# Question 6 - Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

# list1 = [1,5,7,3,5]
# list2 = [1,3,5,7,5]

list1 = ['a','c','b']
list2 = ['c','a','b']
print(permutation(list1, list2))
