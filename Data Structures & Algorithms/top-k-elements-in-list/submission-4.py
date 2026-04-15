class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I know that this is a bucket sort which is the more optimal way to solve this but I don't remember how to solve it
        # We can use a hashMap
        # Store the number as the key and the counts of each number as the value
        # Once we build this map
        # We can go through the map and return the top k elements in a list

        # create a hashmap
        hashMap = defaultdict(int)

        # go thrugh the numbers and get the counts
        for num in nums:
            hashMap[num] += 1 

        # we should have it like this now
        # [1: 1, 2: 2, 3:3]
        # our goal is to return the top 2 values

        # we need to go through each key and compare the values, is there a way to sort the hashMap from least to greatest by the values 
        # use the sorted function
        sorted_items = sorted(hashMap.items(), key=lambda item: item[1])

        sorted_dict = dict(sorted_items)

        result = []

        for i in range(len(sorted_items) -1, len(sorted_items) - 1 - k, -1):
            result.append(sorted_items[i][0])
        
        return result 
