class Solution:
    # use a delimeter to encode and decode ex -> 4#word
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

            # while we haven't encountered the delimeter keep moving j
            while s[j] != "#":
                j += 1 

            # get the length of the word
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        return result
