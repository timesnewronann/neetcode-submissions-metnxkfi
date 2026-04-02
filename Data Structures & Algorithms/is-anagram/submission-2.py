class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the lengths of the strings are the same
        if len(s) != len(t):
            return False # edge case

        #we can use a hashMap and track the letters
        hashMapS = {}
        hashMapT = {}

        # track the letters in s
        for letter in s:
            if letter in hashMapS:
                hashMapS[letter] += 1 
            else:
                hashMapS[letter] = 1

        # track the letter in T
        for letter in t:
            if letter in hashMapT:
                hashMapT[letter] += 1
            else:
                hashMapT[letter] = 1
        
        # compare the count of the letter
        if hashMapS.items() != hashMapT.items():
            return False
        else:
            return True 
