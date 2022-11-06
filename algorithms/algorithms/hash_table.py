class HashTable:
    def __init__(self, table_size = 256):
        self.table_size = table_size
        self.data = [None] * table_size
        
    # The hash function; 
    # this function can be anything you want, 
    # as long as it returns a integer that is within the range(0, talbe_size)
    def _hash(self, str_key):
        v = sum([ord(char) * (index + 1) for (index, char) in enumerate(str_key)])
        return v % self.table_size
        
    def add(self, key, value):
        hash_value = self._hash(key)
        if self.data[hash_value] is None:
            self.data[hash_value] = [(key, value)]
        else:
            self.data[hash_value].append((key, value))
            
    def get(self, key):
        hash_value = self._hash(key)
        if self.data[hash_value] is None:
            return None
        for stored_key, value in self.data[hash_value]:
            if key == stored_key:
                return value
        return None
    
    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        return self.get(key)