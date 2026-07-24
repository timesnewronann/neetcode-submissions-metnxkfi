class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a hashMap with lists to group the words
        # we can build up the words with a result array tracking the letters 
        groups = defaultdict(list)

        for word in strs:
            result = [0] * 26

            for letter in word:
                result[ord(letter) - ord("a")] += 1 
            
            groups[tuple(result)].append(word)

        return list(groups.values())