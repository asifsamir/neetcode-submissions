class Solution:
    def evalRPN(self, tokens) -> int:
        ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a/b)
    }

        cal_list = []
        for token in tokens:
            if token in ops:
                b = cal_list.pop()
                a = cal_list.pop()
                cal_list.append(ops[token](a,b))
            else:
                cal_list.append(int(token))

        return cal_list[0]
