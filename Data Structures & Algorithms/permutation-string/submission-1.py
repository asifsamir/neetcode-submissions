class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        left , right = 0, 0
        for right in range (len(s1), len(s2)): #since we already have the first window, we start from len(s1)
            window[s2[right]] += 1

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if target == window:
                return True

            left += 1

        return False