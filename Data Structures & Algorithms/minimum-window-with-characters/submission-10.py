class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we can use a counter and a dictionary to track the characters that we currently have

        # edge case where t is larger than s
        if len(t) > len(s):
            return ""

        # have a left pointer to adjust a sliding window
        left = 0

        # Track the count of letters we have in a window
        windowDict = defaultdict(int)

        # use a counter to track the letters we have in the t string
        tDict = Counter(t)

        # we also need to track the result which is window size, left, right
        result = [float('inf'), None, None]

        # we want to track our letters we have and the letters we need
        have = 0 
        need = len(tDict)

        for right in range(len(s)):
            windowDict[s[right]] += 1 

            # check if the letter is in our t counter and they have the same counts
            if s[right] in tDict and windowDict[s[right]] == tDict[s[right]]:
                have += 1 

            # while we have enough letters
            while have == need:
                # check if we can shrink our window
                if (right - left + 1) < result[0]:
                    result = [right - left + 1, left, right]

                windowDict[s[left]] -= 1 

                # if the counts of letters are less we have to update have 
                if s[left] in tDict and windowDict[s[left]] < tDict[s[left]]:
                    have -=1 

                left += 1 

        # we can return the result if we have a valid string
        if result[0] != float('inf'):
            return s[result[1]: result[2] + 1]
        else:
            return ""