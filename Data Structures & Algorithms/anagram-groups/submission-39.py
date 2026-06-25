class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for letter in word:
                counts[ord(letter) - ord("a")] += 1 
            
            groups[tuple(counts)].append(word)

        return list(groups.values())