class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will use a hashMap to track the anagrams
        result = defaultdict(list) # track a list of anagrams

        #go through the anagrams
        for anagrams in strs:
            #we can build up the anagrams with a count of the letters
            count = [0] * 26 # 26 letters in alphabet
            #go through each letter 
            for letter in anagrams:
                #increment the count of letters when they appear
                count[ord(letter) - ord("a")] += 1
            #store the count in the anagram as a tuple
            result[tuple(count)].append(anagrams)

        #return the result as a list 
        return list(result.values())