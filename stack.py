# assignment: Programming Assignment 4
# author: Kriti Bhargava
# date: 03/06/2023
# file: stack.py 
# input: The user will enter a simple mathmatical expression 
# output: The calculator will evaluate the function and output the answer. To quit the calculator you enter 'q' or 'quit'

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None