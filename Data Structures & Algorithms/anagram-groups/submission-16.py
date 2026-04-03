from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we should build up a dictionary of lists
        groups = defaultdict(list)

        # go through the word in strs
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            groups[tuple(count)].append(word)
        
        return list(groups.values())

            
            
