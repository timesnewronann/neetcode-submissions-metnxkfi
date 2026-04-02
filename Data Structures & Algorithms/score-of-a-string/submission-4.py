class Solution:
    def scoreOfString(self, s: str) -> int:
        # we use ascii conversion and go through each letter
        # add up the ascii values 
        # return the score

        score = 0

        for i in range(len(s) -1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        

        return score 