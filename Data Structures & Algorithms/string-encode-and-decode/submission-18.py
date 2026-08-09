class Solution:

    # we can track the length of the word and a delimeter to know when to split words
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    # we can take the length of the word and use that to iterate until we hit a delimeter
    def decode(self, s: str) -> List[str]:
        result = []

        i = 0 

        while i < len(s):
            # track j
            j = i

            # check if j is at the delimeter
            while s[j] != "#":
                # move 
                j += 1 

            # get the length of the word
            length = int(s[i:j])

            # update the result with the word from after the delimeter to end of the word
            result.append(s[j + 1: j + 1 + length])

            # move i up to the next word's position
            i = j + 1 + length

        return result
