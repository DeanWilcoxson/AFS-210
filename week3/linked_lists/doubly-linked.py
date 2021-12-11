class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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
        self.count += 1
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

    def addLast(self, data) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail  
            self.tail = node
        self.count += 1        

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        node = Node(data)
        if index > self.count:
            return
        if (index == self.count):
            self.addLast(data)
            return
        if index == 0:
            self.addFirst(data)
            return
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
        node = Node(data)
        prev.next = node
        node.prev = prev
        node.next = curr
        curr.prev = node
        self.count += 1
        return
    
    def replace(self, data, temp):
        index = self.indexOf(temp)
        node = Node(data)
        if (index > (self.count -1)):
            return
        if (index == (self.count -1)):
            self.addLast(data)
            return
        if index == 0:
            self.addFirst(data)
            return
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next        
        prev.next = node
        node.prev = prev
        node.next = curr
        curr.prev = node
        next = curr.next
        curr = curr.prev
        curr.next = next
        return

    def indexOf(self, data):
        curr = self.head
        index = 0
        while curr.next != None:
            if(curr.data == data):
                return index             
            index += 1 
            curr = curr.next
            
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


items = DoublyLinkedList()
items.add("May")
items.add("the")
items.add("Force")
items.add("be")
items.add("with")
items.add("you")
items.add("!")
print(items)
print(items.indexOf("with"))
items.addAtIndex("all", 6)
items.replace("us", "you")
print(items)
