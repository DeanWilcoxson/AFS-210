class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.count = 0
        # self.data = [None] * self.size

    def _hash(self, key):
        # Insert your hashing function code
        return key % self.size

    def _rehash(self, key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self, key, value):
        # Insert your code here to store key and data
        item = HashItem(key, value)
        hash_key = self._hash(key)
        while self.slots[hash_key] is not None:
            if self.slots[hash_key].key is key:
                break
            hash_key = (hash_key + 1) % self.size
        if self.slots[hash_key] is None:
            self.count += 1
        self.slots[hash_key] = item
        print(item)
        return 

    def get(self, key):
        # Insert your code here to get data by key
        hash_key = self._hash(key)
        while self.slots[hash_key] is not None:
            if self.slots[hash_key].key is key:
                return self.slots[hash_key].value
            hash_key = (hash_key + 1) % self.size
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

# Store remaining input data
H = HashTable()
H.__setitem__(69, 'A')
H.__setitem__(66, 'B')
H.__setitem__(80, 'C')
H.__setitem__(35, 'D')
H.__setitem__(18, 'E')
H.__setitem__(52, 'F')
H.__setitem__(89, 'G')
H.__setitem__(70, 'H')
H.__setitem__(12, 'I')


# print the slot values

# print the value for key 52
print(H.__getitem__(69))
print(H._hash(69))
print(H.__getitem__(66))
print(H.__getitem__(80))
print(H.__getitem__(35))
print(H.__getitem__(18))
print(H.__getitem__(52))
print(H.__getitem__(89))
print(H.__getitem__(70))
print(H.__getitem__(12))

