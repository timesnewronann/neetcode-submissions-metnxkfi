class MyHashMap:

    def __init__(self):
        # initialize the object with an empty map
        self.hashMap = [None] * 1000001
        

    def put(self, key: int, value: int) -> None:
        # insert a (key, value) pair in the hashMap
        # first check if the key already exists
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        # if the key doesn't exist return -1
        if self.hashMap[key] is None:
            return -1
      
        return self.hashMap[key]
        

    def remove(self, key: int) -> None:
        # if the map contians mapping key
        self.hashMap[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)