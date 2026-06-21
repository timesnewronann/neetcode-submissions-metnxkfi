class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case where the t > s
        if len(s) < len(t):
            return ""

        # This can be solved with a hashMap and counter
        windowDict = defaultdict(int)
        tDict = Counter(t)

        # we can use a sliding window to track the minimum window substring
        result = [float("inf"), None, None]

        left = 0
        
        # keep track of the letters we have and need
        have = 0
        need = len(tDict)

        # go through the letters in s
        for right in range(len(s)):
            windowDict[s[right]] += 1 
            
            if s[right] in tDict and windowDict[s[right]] == tDict[s[right]]:
                have += 1 

            while have == need:
                # if the current window is smaller than the result window
                if (right - left + 1) < result[0]:
                    result = [right - left + 1, left, right]

                windowDict[s[left]] -= 1 
            
                if s[left] in tDict and windowDict[s[left]] < tDict[s[left]]:
                    have -= 1 
                
                left += 1 
        
        if result[0] != float("inf"):
            return s[result[1]: result[2] + 1]
        else:
            return ""