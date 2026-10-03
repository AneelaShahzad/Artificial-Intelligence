###Q1. Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is already empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is already empty!")

    def size(self):
        return len(self.items)

    def show(self):
        print("Full Stack:", self.items)

    def clear(self):
        for i in len(self.items):
            self.items.pop()
        print("stack is now clear!")

    # def reverse(self):
        

#Example usage:
stack = Stack()

stack.pop()
print(stack.is_empty())
stack.show()

stack.push("Purple")
stack.push("Pink")
stack.push("Blue")

stack.show()
print("Stack Size:", stack.size())
print("Top Element:", stack.peek())
print("Popped Element:", stack.pop())
stack.show()







###Q2. Queue Implementation
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("stack is already empty!")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("queue is empty!")

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("queue is empty!")

    def size(self):
        return len(self.items)

    def show(self):
        print("Full Queue:", self.items)

#Example usage:
queue = Queue()

print(queue.is_empty())
queue.show()

queue.enqueue("Aneela")
queue.enqueue("Arfa")
queue.enqueue("Sara")

queue.show()
print("Queue Size:", queue.size())
print("Front Element:", queue.front())
print("Rear Element:", queue.rear())
print("Dequeued Element:", queue.dequeue())
queue.show()




#q3
#     Perform binary search on a sorted array to find the index of the target value.

#     Parameters:
#     arr (list): A sorted list of elements.
#     target: The value to search for in the array.

#     Returns:
#     int: The index of the target value if found, otherwise -1.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2     #Use integer division

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# #Example usage:
arr = [6, 12, 17, 23, 38, 45, 77, 90]   #Sorted array
target = 45
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")



#take a strung and print it in reverse order using stack
rev_word=Stack()
word="Aneela"
for x in word:
    rev_word.push(x)

print("word : ",word)
print("reverse word :",end=" ")
for x in range(0,len(word)):
    print(rev_word.pop(),end="")