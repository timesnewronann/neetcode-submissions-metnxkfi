class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to group the anagrams using a default dictionary
        result = defaultdict(list)

        #go through the anagrams
        for anagram in strs:
            #keep track of the count of letters to organize the anagrams
            count = [0] * 26
            #go through each letter in each anagram
            for letter in anagram:
                #track the letters
                count[ord(letter) - ord("a")] += 1 
            #store the count in the result
            result[tuple(count)].append(anagram)

        #return the result values as a list
        return list(result.values())