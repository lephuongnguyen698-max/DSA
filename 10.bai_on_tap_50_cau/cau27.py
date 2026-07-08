class QueueWithTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack.pop()

q = QueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())