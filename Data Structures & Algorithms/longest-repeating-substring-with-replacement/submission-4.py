class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_Count = {}
        longest = 0

        l = 0
        r = 0
        max_count = 0

        while r < len(s):
            char_Count[s[r]] = char_Count.get(s[r], 0) + 1

            max_count = max(max_count, char_Count[s[r]])

            if (r - l + 1) - max_count > k:
                char_Count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

            r += 1

        return longest