class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set([])

        l, r, res = 0, 0, 0
        while r < len(s):
            if s[r] in seen:
                seen.clear()
                l += 1
                r = l
            else:
                seen.add(s[r])
                r += 1
                res = max (r - l, res)

        return res
        