class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I think we can solve this question with a hashmap that tracks list
        counts = defaultdict(list)

        # we can go through the string 
        for word in strs:
            result = [0] * 26

            for letter in word:
                result[ord(letter) - ord('a')] += 1 
            
            counts[tuple(result)].append(word)
        
        return list(counts.values())