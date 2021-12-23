class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def keys(self):
        return self.slots

    def values(self):
        return self.data

    def _hash(self, key):
        return key % self.size

    def _rehash(self, key):
        return key // self.size

    def put(self, key, value):
        h_value = self._hash(key)
        if (self.data[h_value] == None):
            self.data[h_value] = value
            self.slots[h_value] = key
        else:
            if(self.slots[h_value] == key):
                self.data[h_value] = value
            else:
                h_value = self._rehash(key)
                if(self.data[h_value] == None):
                    self.data[h_value] = value
                    self.slots[h_value] = key
                else:
                    return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        h_value = self._hash(key)
        if(self.slots[h_value] == key):
            return self.data[h_value]
        else:
            h_value = self._rehash(key)
            if(self.slots[h_value] == key):
                return self.data[h_value]
            else:
                return None
            
            

    def __getitem__(self, key):
        return self.get(key)


# Store remaining input data
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'
# print the slot values
print(H.keys())
# print the data values
print(H.values())
# print the value for key 52
print(H[52])
print(H[80])
print(H[70])
