import numpy as np

# Step 1
print('Step 1')

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ]) # O(1) TC
print(twoDArray)

# Step 2
print('Step 2')
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(twoDArray))

# Step 3
print('Step 3')
newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0) # TC = O(1), simply adding to end of 2d array
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

# Step 4
print('Step 4')

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])
accessElements(twoDArray, 1, 2)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)


# Step 5
print('Step 5')
def traverseTDArray(array):
    for i in range(len(array)): # searches through rows
        for j in range(len(array[0])): # for each row we need to visit all columns
            print(array[i][j])


traverseTDArray(twoDArray)


# Step 6
print('Step 6')
def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element not found'


print(searchTDArray(twoDArray, 14))

# Step 7
print('Step 7')
newTDArray = np.delete(twoDArray, 1, axis=1) # 2nd param is index of row or column, axis 0 = delete first row, axis 1 = deletes first column
print(newTDArray)
