class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can use a hashMap to group the anagrams
        result = defaultdict(list)

        #go through the anagrams
        for anagram in strs:
            count = [0] * 26
            for letter in anagram:
                count[ord(letter) - ord("a")] += 1
            
            result[tuple(count)].append(anagram)
        
        return list(result.values())