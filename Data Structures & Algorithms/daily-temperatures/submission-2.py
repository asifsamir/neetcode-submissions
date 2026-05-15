class Solution:
    def dailyTemperatures(self, temperatures) :
        m_stack = []
        ans = [0]* len(temperatures)

        # left to right monotonic stack
        for i, t in enumerate(temperatures):
            while len(m_stack) > 0 and t > temperatures[m_stack[-1]]:
                loc = m_stack.pop()
                ans[loc] = i - loc

            m_stack.append(i)

        return ans
