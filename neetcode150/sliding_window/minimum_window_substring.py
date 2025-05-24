class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        countT, countWindow = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have, need = 0, len(countT)
        res = ''
        l = 0
        for r in range(len(s)):
            char = s[r]
            countWindow[char] = countWindow.get(char, 0) + 1

            if char in countT and countWindow[char] == countT[char]:
                have += 1
            
            while have == need:
                # Update res
                res = s[l:r + 1] if len(s[l:r + 1]) < len(res) or res == '' else res

                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return res



