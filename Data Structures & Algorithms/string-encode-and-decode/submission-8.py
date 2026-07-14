class Solution:
    # we can track the length of the word and append to with a delimeter to encode
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    # we'll use two pointers to go through the word and add the word into the result str until we reach delimeters
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1 
            
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        
        return result
