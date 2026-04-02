class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to return a list of the anagrams
        result = defaultdict(list)

        #go through the anagrams
        for anagram in strs:
            #create a count of the letters we encounter
            count = [0] * 26
            for letter in anagram:
                #track the letters 
                count[ord(letter) - ord("a")] += 1 

            result[tuple(count)].append(anagram)
        
        return list(result.values())