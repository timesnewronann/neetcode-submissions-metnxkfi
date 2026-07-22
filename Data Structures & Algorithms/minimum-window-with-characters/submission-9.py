class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # goal is to return the shortest substring of s where all characters of t exist in the substring
        # we can use a hashMap to track our currentWindow of letters
        # and we'll use a counter to track the letters in t that we need 

        # edge case what if t > s 
        if len(t) > len(s):
            return ""

        left = 0 

        currWindow = defaultdict(int)

        tDict = Counter(t)

        have = 0
        need = len(tDict)

        result = [float('inf'), None, None]

        for right in range(len(s)):
            currWindow[s[right]] += 1 

            if s[right] in tDict and currWindow[s[right]] == tDict[s[right]]:
                have += 1 

            
            while have == need:
                if (right - left + 1) < result[0]:
                    result = [(right - left + 1), left, right]

                currWindow[s[left]] -= 1 

                if s[left] in tDict and currWindow[s[left]] < tDict[s[left]]:
                    have -= 1 

                left += 1

        
        if result[0] != float('inf'):
            return s[result[1]: result[2] + 1]
        else:
            return ""