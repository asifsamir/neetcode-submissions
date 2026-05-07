class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # clist = list(s)
        # longest = 0

        # i = 0
        # cur_str = list()
        # while (i < len(clist)):

        #     if clist[i] not in cur_str:
        #         cur_str.append(clist[i])
        #         i += 1
        #         continue
        #     else:
        #         longest = max(longest, len(cur_str))

        #         # if i < len(clist) and clist[i] in cur_str:
        #         del cur_str[0: cur_str.index(clist[i]) +1]
        #         cur_str.append(clist[i])
        #         i += 1

        # longest = max(len(cur_str), longest)

        # return longest

        window_chars = {}
        l = 0
        r = 0

        longest = 0

        while (r < len(s)):
            curr_char = s[r]
            if s[r] in window_chars:
                l = max(l, window_chars[s[r]] + 1)

            window_chars[s[r]] = r

            longest = max((r - l + 1), longest)

            r += 1

        return longest


                
