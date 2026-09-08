class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_anagram = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in words_anagram:
                words_anagram[sorted_word] = []
            words_anagram[sorted_word].append(word)
        return words_anagram.values()


            


        