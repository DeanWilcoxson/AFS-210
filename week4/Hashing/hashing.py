class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.count = 0
        # self.data = [None] * self.size

    def _hash(self, key):
        # Insert your hashing function code
        keystr = str(key)
        hashValue = 0
        for character in keystr:
            hashValue += ord(character)
        return (hashValue*len(keystr)) % self.size

    def _rehash(self, key):
        # Insert your secondary hashing function code
        keystr = str(key)
        multiplier = 1
        hashValue = 0
        for character in keystr:
            hashValue += multiplier * ord(character)
            multiplier += 1
        return (hashValue*len(keystr)) % self.size

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

H = HashTable()
H[69] = 'A'

# Store remaining input data

# print the slot values

# print the data values

# print the value for key 52
