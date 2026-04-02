class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We can use a hashMap to group up the letters 
        groups = defaultdict(list)

        for s in strs:
            #track the letters with alphabet
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 
            
            groups[tuple(count)].append(s)

        return list(groups.values())