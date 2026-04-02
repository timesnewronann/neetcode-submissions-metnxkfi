class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we can count the letters and make sure that the counts are the same
        #if the string lengths aren't the same can't be an anagram
        if len(s) != len(t):
            return False

        hashMapS = {}
        hashMapT = {}

        for letter in s:
            if letter in hashMapS:
                hashMapS[letter] += 1 
            else:
                hashMapS[letter] = 1 
        
        for letter in t:
            if letter in hashMapT:
                hashMapT[letter] += 1
            else:
                hashMapT[letter] = 1

        #compare the two hashMap
        if hashMapS.items() != hashMapT.items():
            return False 
        else:
            return True 