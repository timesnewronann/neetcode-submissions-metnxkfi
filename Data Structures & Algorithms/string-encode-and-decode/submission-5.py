class Solution:

    # we can keep track of the length of the word and add a delimeter to the combined string
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    #4#word5#words -> [word, words]

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0 

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1 # keep moving forward until we reahc one

            # track the length of the characters we need to read through
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])

            i = 1 + j + length

        return result