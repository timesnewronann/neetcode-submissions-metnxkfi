class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for letter in s:
            if letter in hashMap:
                hashMap[letter] += 1 

            else:
                hashMap[letter] = 1

        # go through each letter
        for i in range(len(s)):
            if hashMap[s[i]] == 1:
                return i

        return -1