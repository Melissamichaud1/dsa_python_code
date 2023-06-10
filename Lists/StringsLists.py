# List() - string to list
print('List()')
a = 'example'
b = list(a)
print(b)

# Split()
print('Splitting')
c = 'example example'
d = c.split()
print(d)

# Delimiter
print('Delimiter')
e = 'example-example1'
delimiter = '-'
f = e.split(delimiter)
print(f)
# Join() - list to string
print('Join()')
print(delimiter.join(f))
