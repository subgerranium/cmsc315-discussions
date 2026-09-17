"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Newest value is added to top, so it will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, return None instead of erroring out.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek lets us see the newest added value without actually removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so the first value added will be the first removed (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # If the queue is empty, return None instead of erroring out.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the first value of the queue without removing.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")

# Stack for browser history
fruit_bowl = Stack()

# Add 4 values to the stack
fruit_bowl.push("Apple")
fruit_bowl.push("Banana")
fruit_bowl.push("Orange")
fruit_bowl.push("Peach")

print("Fruit were added to the fruit bowl stack.")
print("The most recent fruit added will be removed first because this stack uses LIFO.")

# Peek the newest fruit without removing.
print("Last fruit before popping:", fruit_bowl.peek())

# Show LIFO behavior by removing fruit
print("Popped:", fruit_bowl.pop())
print("Popped:", fruit_bowl.pop())
print("Popped:", fruit_bowl.pop())
print("Popped:", fruit_bowl.pop())

# Test pops from an empty stack.
print("      test popping from an empty stack,")
print("Pop from an empty stack:", fruit_bowl.pop())

# Test peek with an empty stack.
print("      test peeking at an empty stack,")
print("Peek at an empty stack:", fruit_bowl.peek())

# Test a stack with only one item.
print("      and verify a single-item stack becomes empty after removal.")
single_stack = Stack()
single_stack.push("Only Item")

print("Single item before removal is empty:", single_stack.is_empty())

single_stack.pop()

print("Single item after removal is empty:", single_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
bakery = Queue()

# Adding 4 customers to line.
bakery.enqueue("Customer 1")
bakery.enqueue("Customer 2")
bakery.enqueue("Customer 3")
bakery.enqueue("Customer 4")

print("4 customers have joined the bakery queue.")
print("The first customer to arrive will be served first because the queue uses FIFO.")

# See the next customer without removing them.
print("Customer in front:", bakery.front())

# Show FIFO by removing customers.
print("Served:",bakery.dequeue())
print("Served:",bakery.dequeue())
print("Served:",bakery.dequeue())
print("Served:",bakery.dequeue())

# Test dequeuing from an empty line.
print("      test dequeuing from an empty queue,")
print("Dequeued from empty:",bakery.dequeue())

# Test viewing the front of an empty line.
print("      test viewing the front of an empty queue,")
print("Front of empty queue:", bakery.front())

# Test queue with only 1 item.
print("      and verify a single-item queue becomes empty after removal.")
single_queue = Queue()
single_queue.enqueue("Only Customer")

print("Single item queue before removal is empty:", single_queue.is_empty())

single_queue.dequeue()

print("Single item queue after removal is empty:", single_queue.is_empty())

if __name__ == "__main__":
    main()
