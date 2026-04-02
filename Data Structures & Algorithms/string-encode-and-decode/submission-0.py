class Solution:

    def encode(self, strs: List[str]) -> str:
        #Encode the list of strings into a single string
        res = ""

        for s in strs:
            #append string into result
            #length + delimeter + string
            res += str(len(s)) + "#" + s

        return res 

    def decode(self, s: str) -> List[str]:
        #Given a single str decode into list of strings
        #List and index to see where we are at in the list of strings
        res = []
        i = 0

        #Go character by character
        while i < len(s):
            #find the delimeter, end of int
            j = i

            while s[j] != "#": #we're still not at the delimeter
                j += 1
            #We get to delimeter
            length = int(s[i:j]) #go all the way to j but not including 

            #j + 1 first character after delimeter 
            #gives us entire string
            res.append(s[j+1: j + 1 + length])

            #move i, beginning of next string or end of entire string
            i = j + 1 + length 

        return res

