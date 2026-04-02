class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use a default dict to store the anagrams
        result = defaultdict(list)

        #go through each word
        for word in strs:
            #create a count of each letter abc (26 letters)
            count = [0] * 26
            #go through the letters in each word
            for letter in word:
                #ascii ord to track count of each letter
                count[ord("c") - ord(letter)] += 1
            #store the count in result
            result[tuple(count)].append(word)
        return list(result.values())
                
