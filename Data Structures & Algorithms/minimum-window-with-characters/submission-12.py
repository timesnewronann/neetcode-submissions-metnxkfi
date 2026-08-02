class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we can use a sliding window to check the window
        # and use a dictionary to track the curr letters we have
        # and a counter to check the letters we need

        # edge case where the len t > len s
        if len(s) < len(t):
            return ""

        left = 0
        windowDict = defaultdict(int)
        tDict = Counter(t)

        result = [float("inf"), None, None]
        have = 0
        need = len(tDict)

        for right in range(len(s)):
            windowDict[s[right]] += 1 

            if s[right] in tDict and windowDict[s[right]] == tDict[s[right]]:
                have += 1 

            while have == need:
                # check if we can shrink our window
                if (right - left + 1) < result[0]:
                    result = [(right - left + 1), left, right]

                windowDict[s[left]] -= 1 

                if s[left] in tDict and windowDict[s[left]] < tDict[s[left]]:
                    have -=1 

                left += 1 
            
        
        if result[0] != float("inf"):
            return s[result[1]: result[2] + 1]
        
        else: 
            return ""