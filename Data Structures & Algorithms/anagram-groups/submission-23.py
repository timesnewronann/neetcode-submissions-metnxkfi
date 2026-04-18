class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a dictionary to track the grouped words
        groups = defaultdict(list)

        for word in strs:
            # track the counts of the letters
            result = [0] * 26

            # go through each letter in the word
            for letter in word:
                result[ord(letter) - ord("a")] += 1 
            
            # add each grouped anagram into the hashmap
            groups[tuple(result)].append(word)

        # return the hashMap's values
        return list(groups.values())