class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We are gonna map the anagrams by a key using a key
        groups = defaultdict(list) 

        #Go through each anagram
        for s in strs:
            #create a key of the anagrams sorted
            key = "".join(sorted(s)) #O(logn)
            #build up the group with key and store it in groups
            groups[key].append(s)
        
        return groups.values()