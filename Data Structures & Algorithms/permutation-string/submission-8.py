class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def get_ascii(ch):
            return ord(ch)-ord('a')

        if len(s1) > len(s2):
            return False

        target = [0]*26
        window = [0]*26

        for ch in s1:
            target[get_ascii(ch)] += 1

        for i in range(len(s1)):
            window[get_ascii(s2[i])] += 1

        if target == window:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[get_ascii(s2[right])] += 1
            window[get_ascii(s2[left])] -= 1

            if window == target:
                return True

            left += 1

        return False
