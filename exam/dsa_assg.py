#Q. 1 Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display
# 4. Reverse String using Stack
# 5. Reverse Stack using another Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped:", self.stack.pop())

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", self.stack)

    def reverse_string(self, string):
        s = []
        for ch in string:
            s.append(ch)
        result = ""
        while s:
            result += s.pop()
        print("Reversed string:", result)

    def reverse_stack(self):
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        self.stack = temp
        print("Stack reversed")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
s.reverse_string("PYTHON")
s.reverse_stack()
s.display()