from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # Each anagram has a unique character count array
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - 97] += 1

            # Map strings to their associated character count array
            res[tuple(char_count)].append(s)

        # Return character count groups
        return res.values()

        