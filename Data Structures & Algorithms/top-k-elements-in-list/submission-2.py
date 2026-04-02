class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We'll use a bucket sort with a hashMap
        #We'll also use a frequency array to track the numbers which occur a certain frequency
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        #go through the list of numbers and track the frequency
        for num in nums:
            counts[num] = 1 + counts.get(num, 0) #default value of 0 for dne
            
        #go through each counted value
        for number, count in counts.items():
            #insert the number into the frequency array 
            frequency[count].append(number)

        #create our result array that we'll return 
        result = []

        #Get the largest frequency first so go through frequency backwards
        for i in range(len(frequency) - 1, 0, -1):
            #go through every value 
            for number in frequency[i]:
                #build our result array
                result.append(number)
                #To check if we have top k elements
                if len(result) == k:
                    return result