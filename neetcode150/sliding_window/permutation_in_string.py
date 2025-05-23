class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Determine char freq of s1
        freqS1 = {}
        for char in s1:
            freqS1[char] = freqS1.get(char, 0) + 1

        l = 0
        freqWindow = {}
        for r in range(len(s2)):

            # Add char to frequency dict
            freqWindow[s2[r]] = freqWindow.get(s2[r], 0) + 1

            # If the window's size is less than the size of s1
            if r - l + 1 < len(s1):
                continue
            
            # If the window's freq dict matches s1 freq dict, its a permutation
            if freqWindow == freqS1:
                return True

            # Slide window over by 1, updating window char freq
            freqWindow[s2[l]] -= 1
            if freqWindow[s2[l]] == 0:
                del freqWindow[s2[l]]
            l += 1
        return False

        