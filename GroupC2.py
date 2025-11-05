class Bucket:
    def __init__(self, size):
        self.size = size
        self.keys = []

    def is_full(self):
        return len(self.keys) >= self.size

    def insert(self, key):
        if not self.is_full():
            self.keys.append(key)
            return True
        return False

    def search(self, key):
        return key in self.keys

    def delete(self, key):
        if key in self.keys:
            self.keys.remove(key)
            return True
        return False

class ExtendibleHashTable:
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.global_depth = 1
        self.directory = [Bucket(bucket_size) for _ in range(2 ** self.global_depth)]
    
    def hash_function(self, key):
        return key & ((1 << self.global_depth) - 1)

    def double_directory(self):
        self.directory += self.directory
        self.global_depth += 1

    def insert(self, key):
        index = self.hash_function(key)
        bucket = self.directory[index]
        if not bucket.insert(key):
            self.double_directory()
            self.insert(key)  

    def search(self, key):
        index = self.hash_function(key)
        return self.directory[index].search(key)

    def delete(self, key):
        index = self.hash_function(key)
        return self.directory[index].delete(key)

    def display(self):
        for i, bucket in enumerate(self.directory):
            print(f"Index {i}: {bucket.keys}")


eht = ExtendibleHashTable(2)
eht.insert(10)
eht.insert(20)
eht.insert(30)
print("Search 20:", eht.search(20))
eht.delete(20)
eht.display()
