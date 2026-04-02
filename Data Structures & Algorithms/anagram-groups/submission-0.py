from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Input: array of strings
        #Group the anagrams into sublists 
        #Return the output does not need to be ordered

        #We could check for anagrams with the two hashmaps
        #But that isn't optimal

        #We could sort the strs and check if they're equal
        #organize them into groups of anagrams a list of string
        groups = defaultdict(list)

        
        #go through the strs
        for s in strs:
            #Create an identifier of the sorted key to compare it 
            #We will use this to compare the anagrams and group them
            key = "".join(sorted(s))
            #add the sorted keys into the groups, use the key as the key for the map
            groups[key].append(s)

        return groups.values()

        


