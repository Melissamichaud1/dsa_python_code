# Same as array

shoppingList = ['Milk', 'Bread', 'Eggs']

# Access
print(shoppingList[1])

# Traverse
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
