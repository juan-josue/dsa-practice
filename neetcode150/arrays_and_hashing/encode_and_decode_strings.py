from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoded strings are the len of the str following by #
        # Example: ["hello", "world"] -> "5#hello5#world"
        res = ''
        for s in strs:
            s_encoded = str(len(s)) + '#' + s
            res += s_encoded
        return res

    def decode(self, s: str) -> List[str]:
        # Decode the string by finding the length of each str
        # Example: ["hello", "world"] <- "5#hello5#world"
        res = []
        i = 0
        
        while i < len(s):
            j = s.index('#', i)
            len_str = int(s[i : j])
            res.append(s[j + 1 : j + len_str + 1])
            i = j + len_str + 1
        return res

