class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams must be the same len
        if len(s) != len(t):
            return False
        
        # Initiaize char freq dict
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        
        # Values will be 0 if the frequencies were equal
        for key in freq:
            if freq[key] != 0:
                return False
        return True