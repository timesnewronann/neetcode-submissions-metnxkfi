class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can group the anagrams with a hashMap and create a count of the alphabet
        result = defaultdict(list)

        #go through the anagrams
        for anagram in strs:
            #create a count of the letters for each anagram
            count = [0] * 26
            for letter in anagram:
                #we will build up the alphabet
                count[ord(letter) - ord("a")] += 1 # track the letters
            result[tuple(count)].append(anagram)

        return list(result.values())