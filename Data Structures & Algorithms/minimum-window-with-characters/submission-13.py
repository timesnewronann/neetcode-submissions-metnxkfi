class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # goal is to return the minimum window substring within s from t
        # edge case what if t len > s len -> return an empty string
        
        if len(s) < len(t):
            return ""

        # use a hashmap to track our currentwindow
        windowDict = defaultdict(int)
        # use a counter to track the tdict
        tDict = Counter(t)

        # we can track the result [the length of the window, left, right]
        result = [float('inf'), None, None]

        left = 0 
        
        # track the count of letters we have and need
        have = 0
        need = len(tDict)

        # go through the string
        for right in range(len(s)):
            # add the currentwindow up
            windowDict[s[right]] += 1 

            # if the count is the same
            if s[right] in tDict and windowDict[s[right]] == tDict[s[right]]:
                # increment our have
                have += 1 

            # we have enough count to shrink
            while have == need:
                # check the result
                if (right - left + 1) < result[0]:
                    result = [(right - left + 1), left, right]
                
                windowDict[s[left]] -= 1

                if s[left] in tDict and windowDict[s[left]] < tDict[s[left]]:
                    have -= 1 
                
                left += 1
            
        if result[0] != float('inf'):
            return s[result[1]: result[2] + 1]
        else:
            return ""