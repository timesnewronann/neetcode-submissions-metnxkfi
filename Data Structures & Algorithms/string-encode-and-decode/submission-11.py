class Solution:
    # we can use a delimeter and the length of the word to determine when the next word starts
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                # keep moving forward till we get the end of the word
                j += 1 
            
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        
        return result
