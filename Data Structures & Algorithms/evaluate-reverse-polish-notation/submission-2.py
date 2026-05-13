class Solution:
    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens) -> int:

        cal_list = []
        for num in tokens:
            if self.is_integer(num):
                cal_list.append(int(num))
            else:
                b = cal_list.pop()
                a = cal_list.pop()

                if num == '+':
                    cal_list.append(a + b)
                elif num == '-':
                    cal_list.append(a - b)
                elif num == '*':
                    cal_list.append(a * b)
                elif num == '/':
                    cal_list.append(int(a / b))

        return cal_list[0]
