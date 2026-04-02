class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we'll use a hashMap forsure
        # we want to look at the individual anagram in the groups, 
        #look at the characters and 
        # look at the frequency of each character in a string
        # we look at the frequency because the anagrams have the same counts of letters 
        
        # we want a dictionary of lists to store individual hashMaps
        hashMap = defaultdict(list)

        
        # use this array as the key in the hashMap to group strings 
        # go through the anagrams
        for anagrams in strs:
            # use an array of the alphabet size to count frequency in the string
            counts = [0] * 26
            # go through the letters in the individual anagram
            for letter in anagrams:
                # store the letters into the count
                counts[ord(letter) - ord('a')] += 1
            #store the count in our hashMap 
            hashMap[tuple(counts)].append(anagrams)
        return list(hashMap.values())