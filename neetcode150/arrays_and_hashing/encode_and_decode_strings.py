from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            s_encoded = str(len(s)) + '#' + s
            res += s_encoded
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.index('#', i)
            len_str = int(s[i : j])
            res.append(s[j + 1 : j + len_str + 1])
            i = j + len_str + 1
        return res

