class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a hashmap tracking lists to track all the words that are groups
        groups = defaultdict(list)

        # we can build up the words through an array
        for word in strs:
            result = [0] * 26

            # go through each letter in the word
            for letter in word:
                # build the count of letters up so we can group
                result[ord(letter) - ord("a")] += 1 

            # add the word as a value with the key being all the letters
            groups[tuple(result)].append(word)

        return list(groups.values())



