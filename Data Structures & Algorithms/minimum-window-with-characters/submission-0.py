from collections import Counter 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case if no substring exists return empty array
        if len(s) < len(t):
            return ""

        # we can use a hashMap to track the frequency of letters we have and letters we need
        tDict = Counter(t)
        haveDict = defaultdict(int)

        have = 0
        need = len(tDict)

        result = [float('inf'), None, None] #result, left, right 
        left = 0 

        for right in range(len(s)):
            #always increment the haveDict
            haveDict[s[right]] += 1
            if s[right] in tDict and haveDict[s[right]] == tDict[s[right]]:
                # I have matched all required instances of this character
                have += 1
            
            #while we have all letters we have a valid window
            while have == need:
                # save the result
                if (right - left + 1) < result[0]:
                    result = [right - left + 1, left , right]
                # see if we can shrink the window
                haveDict[s[left]] -= 1 
                if s[left] in tDict and haveDict[s[left]] < tDict[s[left]]:
                    have -= 1 
                
                left += 1 
        
        if result[0] != float('inf'):
            return s[result[1]:result[2] +1]
        else:
            return ""


