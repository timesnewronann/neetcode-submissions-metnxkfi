class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a defaultdict that tracks lists to group the words together
        groups = defaultdict(list)

        # go through the words in the list of the strings
        for word in strs:
            # abcs 
            result = [0] * 26 

            for letter in word:
                # store the counts of each letter
                result[ord(letter) - ord("a")] += 1 
            
            # after tracking counts store the groups of words
            groups[tuple(result)].append(word)
        
        return list(groups.values())