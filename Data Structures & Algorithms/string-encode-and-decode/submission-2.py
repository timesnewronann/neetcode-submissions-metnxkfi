class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want to mark the strs with the length of the string and a delemiter

        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = i

            # while we aren't on a delimeter
            while s[j] != "#":
                j += 1 
            
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])

            # beginning/end of the next string
            i = j + 1 + length

        return result
