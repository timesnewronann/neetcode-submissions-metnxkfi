class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        #Input array will determine the length of the hashMap
        #For the index of the hashmap we'll map the count of values 
        #For the value it will be a list where which values have that count
        #Top K go backwards on count and append the values to the result array 
        #O(n)

        #Create the hashMap to count occurences
        count = {}

        #array that's the same size as input array
        freq = [[]for i in range(len(nums) + 1)]

        #go through every value and count every occurence 
        for n in nums:
            count[n] = 1 + count.get(n,0) #if count doesn't exist 0 is default 
        
        #Go through each counted value
        for number, count in count.items():
            #in the frequency insert 
            freq[count].append(number) #this value occurs the count amount of times

        res = []

        #go through the frequency backwards
        for i in range(len(freq) -1 , 0, -1):
            #go through every value in the freq
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        
    