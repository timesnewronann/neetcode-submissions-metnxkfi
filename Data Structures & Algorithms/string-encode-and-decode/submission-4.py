class Solution:

    # we can use an integer and a delimeter to track how many chars are in a word and the delimeter to separate words
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        # we want the original decoded list
        result = []

        # we can use two pointers to track the characters in the string
        i = 0

        # loop while i inbounds
        while i < len(s):
            j = i 

            # if we haven't encountered the delimeter
            while s[j] != "#":
                j += 1 # keep moving the pointer forward 

            # track the length of the amount of characters we need to read 
            length = int(s[i:j])

            # store each word in the list
            result.append(s[j + 1 : j + 1 + length])

            # move i to the start of the next word
            i = 1 + j + length


        return result


