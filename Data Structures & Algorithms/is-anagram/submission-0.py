class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = {}
        anagram_t = {}

        for let_s in s:
            if let_s in anagram_s:
                anagram_s[let_s] += 1
            else:
                anagram_s[let_s] = 1
        
        for let_t in t:
            if let_t in anagram_t:
                anagram_t[let_t] += 1
            else:
                anagram_t[let_t] = 1

        if anagram_s == anagram_t:
            return True
        else:
            return False
        
        