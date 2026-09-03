class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # goal is to return the minimum window substring from s that contains all letters of t

        # edge case what if the len(t) > len(s)
        if len(s) < len(t):
            return ""

        # we can use a hashmap to track the window size of the letters we have
        currWindow = defaultdict(int)

        # track the tDict letters
        tDict = Counter(t)

        # we can use a sliding window to the get the min window
        result = [float('inf'), None, None]

        left = 0
        
        # track the letters we have and need
        have = 0
        need = len(tDict)

        # go through the letters in s
        for right in range(len(s)):
            # add up the window
            currWindow[s[right]] += 1 

            if s[right] in tDict and currWindow[s[right]] == tDict[s[right]]:
                # incrment the count of letters we have
                have += 1 

            # while we have enough letters to shrink the windwo
            while have == need:
                # check if we can shrink the window
                if (right - left + 1 < result[0]):
                    result = [right - left + 1, left, right]

                # decrement the window
                currWindow[s[left]] -= 1 

                if s[left] in tDict and currWindow[s[left]] < tDict[s[left]]:
                    have -= 1 

                left += 1
        
        if result[0] != float('inf'):
            return s[result[1]: result[2] + 1]
        else:
            return ""