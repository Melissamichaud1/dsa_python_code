total = 0
count = 0
while (True):
    inp = input('Enter a number. If you are done, type done: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print('Average:', average)

# Convert using list functions
lst = []
while (True):
    inp = input('Enter a number. If you are done, type done: ')
    if inp == 'done': break
    lst.append(float(inp))
    avg = sum(lst) / len(lst)

print('Average:', avg)
