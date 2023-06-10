class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = list(reversed(self.list))
        values = [str(x) for x in values]
        return '\n'.join(values)

    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop - remove last eleemnt in the stack
    def pop(self):
        if self.isEmpty():
            return "There are no elements in this stack"
        else:
            return self.list.pop()

    # peek - returns last element in the stack
    def peek(self):
        if self.isEmpty():
            return "There are no elements in this stack"
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = None



customStack = Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
# print(customStack.pop())
print(customStack.peek())
print(customStack)
