class Solution:
    # logic behind this question
    # We will store the length of each string with and delimeter
    # example "Hello", "World" -> "5#Hello5#World -> so we know how many letters to go through after the delimeter
    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        # we want the list of strings
        result = []

        i = 0

        # read character by character
        while i < len(s):
            # find the delemiter
            j = i 

            # while we haven't reached the delimeter
            while s[j] != "#":
                j += 1 
            
            # how many characters we need to read after j to get the characters of the string
            length = int(s[i:j])

            # get every character of the string
            # start from the first character in the string all the way to the end of the string
            result.append(s[j + 1: j + 1 + length])

            # move i to the next word
            # beginning of the next string or end of the string
            i = j + 1 + length


        return result

