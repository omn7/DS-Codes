class HashTb:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key% self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index+1)%self.size
        self.table[index] = key
    def search(self, key):
        index = self.hash_function(key)
        start = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index+1)%self.size
            if start == index:
                break
        return -1
    
    def delete(self, key):
        index = self.search(key)
        if index == -1:
            print("Key not found.")
            return
        self.table[index] = None
       
        old_table = self.table[:]
        self.table = [None] * self.size
        for item in old_table:
            if item is not None:
                self.insert(item)
        print(f"Key {key} deleted.")
    
    def display(self):
        for i,key in enumerate(self.table):
            print(f"index {i}: {key}")

ht = HashTb(10)
ht.insert(10)
ht.insert(20)
ht.insert(30)
print("Searching for 20:", ht.search(20))
ht.delete(20)
ht.display()


       

            
            
            


