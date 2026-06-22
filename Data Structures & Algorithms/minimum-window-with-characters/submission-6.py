class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # This question's goal is to return the minimum window substring
        # between t and s
        # we can use a hashmap to track our current window -> windowDict
        # We can use a counter to track the letters in T

        # there's a edge case where the length of t is greater than s 
        # so that substring wouldn't exist
        if len(s) < len(t):
            return ""

        # define our datastructures
        windowDict = defaultdict(int)
        tDict = Counter(t)

        result = [float("inf"), None, None] # window size, left, right
        left = 0 

        have = 0 
        need = len(tDict)

        for right in range(len(s)):
            windowDict[s[right]] += 1 

            if s[right] in tDict and windowDict[s[right]] == tDict[s[right]]:
                have += 1 
            
            while have == need:
                if (right - left + 1 ) < result[0]:
                    result = [right - left + 1, left, right]
                
                windowDict[s[left]] -= 1

                if s[left] in tDict and windowDict[s[left]] < tDict[s[left]]:
                    have -= 1
                
                left += 1 
            
        
        # return the result
        if result[0] != float("inf"):
            return s[result[1]: result[2] + 1]
        else:
            return ""