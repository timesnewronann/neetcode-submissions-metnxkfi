class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            result = [0] * 26

            for letter in word:
                # build up the count of letters we'll group
                result[ord(letter) - ord("a")] += 1 

            # group the words together in our map
            groups[tuple(result)].append(word)

        return list(groups.values())