class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # how would I solve this brute force
        # I could go through 

        prefix = ""

        # go through each character in strs
        for i in range(len(strs[0])):
            # go through each string and make sure that i has the same character
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            
            prefix += strs[0][i]
            

        return prefix