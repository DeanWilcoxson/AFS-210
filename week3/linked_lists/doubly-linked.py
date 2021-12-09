class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def size(self) -> int:
        return self.count

    def addFirst(self, data) -> None:
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None
        self.count += 1

    def addLast(self, data) -> None:
        node = Node(data)
        self.tail.prev = node
        self.tail = node
        node.next = None
        self.count += 1

    # def addAtIndex(self, data, index):
        node = Node(data)
        
    # def indexOf(self, data):

    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        if (index > (self.count-1)):
            return
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1
        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev
        return

    def delete(self, data) -> None:
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node) + " "
        return myStr
