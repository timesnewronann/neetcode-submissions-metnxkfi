class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a hashMap of lists to track the groups of words
        groups = defaultdict(list)

        # go through the word in strs
        for word in strs:
            # we want to use a result array to track the letters for each group
            result = [0] * 26

            # go through the letters in each word
            for letter in word:
                # build up the letters for the word
                result[ord(letter) - ord("a")] += 1 

            # add the letters into our group hashMap
            groups[tuple(result)].append(word)
        
        return list(groups.values())