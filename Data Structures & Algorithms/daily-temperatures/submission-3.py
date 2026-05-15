class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m_stack = []
        ans = [0]* len(temperatures)
        top = -1

        # right to left monotonic stack
        for i in range (len(temperatures)-1, -1 , -1):
            ct = temperatures[i]

            if top == -1:
                m_stack.append((ct, i))
                ans[i] = 0
                top += 1
            else:
                if ct < m_stack[top][0]:
                    m_stack.append((ct, i))
                    ans[i] = m_stack[top][1] - i

                    top += 1
                else:
                    while top > -1 and ct >= m_stack[top][0] :
                        m_stack.pop()
                        top -= 1

                    m_stack.append((ct, i))
                    ans[i] = 0 if top == -1 else m_stack[top][1] - i
                    top += 1

        return ans

                    

        