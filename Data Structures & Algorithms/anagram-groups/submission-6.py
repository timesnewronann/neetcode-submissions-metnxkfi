class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to group the anagrams by the count of of letters
        # we can build up our own alphabet array and store the letters that way
        hashMap = defaultdict(list) # use a dictionary that stores list to sort our anagrams

        for anagrams in strs:
            #create a count of the alphabet
            count = [0] * 26
            #go through each letter in the individual anagrams
            for letter in anagrams:
                #store the count of letters
                count[ord(letter) - ord('a')] += 1 
            hashMap[tuple(count)].append(anagrams)

        return list(hashMap.values())