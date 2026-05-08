class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
            
        target = [0]*256
        window = [0]*256

        for ch in s1:
            target[ord(ch)] += 1

        for i in range(len(s1)):
            window[ord(s2[i])] += 1

        if target == window:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[ord(s2[right])] += 1
            window[ord(s2[left])] -= 1

            if window == target:
                return True

            left += 1

        return False
