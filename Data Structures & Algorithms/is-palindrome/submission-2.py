class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_len = len(s)

        start_index = 0
        end_index = str_len - 1

        if str_len == 0:
            return True

        while start_index < end_index:
            while not s[start_index].isalnum() and start_index < end_index:
                start_index += 1

            while not s[end_index].isalnum() and start_index < end_index :
                end_index -= 1

            if start_index > end_index:
                return True

            if s[start_index].casefold() != s[end_index].casefold():
                return False

            start_index += 1
            end_index -= 1

        return True