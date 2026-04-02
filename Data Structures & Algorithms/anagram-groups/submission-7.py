class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashMap and build up the letter with an array
        hashMap = defaultdict(list)

        #go through the anagrams
        for anagram in strs:
            #create the alphabet
            count = [0] * 26
            for letter in anagram:
                count[ord(letter) - ord("a")] += 1
            hashMap[tuple(count)].append(anagram)

        return list(hashMap.values())