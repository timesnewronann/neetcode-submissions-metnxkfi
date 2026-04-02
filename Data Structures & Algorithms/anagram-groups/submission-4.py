class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We can do this without sorting the list
        groups = defaultdict(list)

        #use counts 
        for s in strs:
            counts = [0] * 26 
            for c in s:
                counts[ord(c) - ord("a")] += 1 
            #track each count in the group
            groups[tuple(counts)].append(s)

        return groups.values()
            