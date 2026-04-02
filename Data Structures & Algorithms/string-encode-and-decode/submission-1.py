class Solution:
    #We'll use a delimeter and the number of letters after to encode and decode 
    def encode(self, strs: List[str]) -> str:
        #build our result str
        result = ""

        #go through the input strs
        for s in strs:
            #the number of letters + a delimeter + og string
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        #We get a string with a delimeter and we need to break it down into a list
        #result array
        result = []

        #index postion
        i = 0

        #while in bounds of the str/ don't exceed string length
        while i < len(s):
            #find the delimeter end of int
            j = i
            while s[j] != "#":
                j+= 1
            #Eventually get to the delimeter
            #Our length is the everything but j
            length = int(s[i:j])

            #J + 1 first character after delimeter
            result.append(s[j+1: j+ 1 + length])

            #move i to the start of the next string
            i = j + 1 + length

        return result
