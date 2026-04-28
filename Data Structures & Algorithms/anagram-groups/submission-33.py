class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a hashMap to track the groups of words
        groups = defaultdict(list)

        # go through each word in our list
        for word in strs:
            # create a list of the letters to track each letter so we can group up the anagrams
            result = [0] * 26

            for letter in word:
                result[ord(letter) - ord("a")] += 1 
            
            groups[tuple(result)].append(word)

        return list(groups.values())