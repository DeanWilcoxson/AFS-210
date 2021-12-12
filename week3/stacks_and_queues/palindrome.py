class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)
        return

    def pop(self):
        return self.stack.pop(0)

    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        if(len(self.stack) <= 0):
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        data = self.queue.pop()
        return data

    def getSize(self):
        return len(self.queue)

    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

def isPalindrome(str):
    stack = Stack()
    queue = Queue()
    for ch in str:
        stack.push(ch)
        queue.enqueue(ch)
        if(stack.isEmpty() != True):
            for x in stack.stack:
                stackLetter = stack.pop()
                queueLetter = queue.dequeue()
                if(stackLetter == queueLetter):
                    return True
                else:
                    return False

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))
