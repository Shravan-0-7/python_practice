# Q. 2 Write a program to perform the following operations on a Linear
# Queue
# 1. Enqueue an element into the queue
# 2. Dequeue an element from the queue
# 3. Display
# 4. Reverse the queue using stack
# 5. Merge two queues into one.
# 6. Check if two queues are identical

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted:", self.queue.pop(0))

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed")

    def merge(self, q2):
        self.queue.extend(q2.queue)
        print("Queues merged")

    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are identical")
        else:
            print("Queues are not identical")
q1 = Queue()
q2 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q2.enqueue(40)
q2.enqueue(50)
q1.display()
q2.display()
q1.dequeue()
q1.display()
q1.reverse_queue()
q1.display()
q1.merge(q2)
q1.display()
q1.identical(q2)