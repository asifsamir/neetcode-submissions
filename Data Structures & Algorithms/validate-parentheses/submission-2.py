class Solution:
    def isValid(self, s: str) -> bool:

        dict_br = {
            '(': 1,
            '{': 2,
            '[': 3,
            ')': -1,
            '}': -2,
            ']': -3,
        }
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        stack = []
        cumul = 0

        for c in s:
            if dict_br[c] > 0:
                stack.append(c)
                cumul += dict_br[c]
            else:
                if len(stack)== 0:
                    return False
                top = stack.pop()
                if dict_br[top] + dict_br[c] != 0:
                    return False
                cumul += dict_br[c]

        if cumul != 0:
            return False


        return True
