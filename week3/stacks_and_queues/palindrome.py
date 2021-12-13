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
        if(len(self.queue) < 1):
            return True
        else:
            return False

    def peek(self):
        if(len(self.queue) > 0):
          return self.queue[-1]
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
                stackLetter = stack.peek()
                queueLetter = queue.peek()
                if(stackLetter == queueLetter):
                    stack.pop()
                    queue.dequeue()
                else:
                    return False
        return True

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))
