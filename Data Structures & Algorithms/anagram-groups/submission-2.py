class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            #create a key to track the groups
            key = "".join(sorted(s))

            #use this key to map the anagrams
            groups[key].append(s)

        return groups.values()