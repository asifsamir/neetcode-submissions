class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # max_w = 0

        # for i, h in enumerate(heights):
            
        #     j = len(heights) - 1
        #     while j > i and j < len(heights):
        #         temp_w = (j - i) * min(heights[i], heights[j])

        #         if temp_w > max_w:
        #             max_w = temp_w

        #         j -= 1


        # return max_w

        i = 0
        j = len(heights) - 1
        maxW = 0
        
        while i < j:
            w = (j - i) * min(heights[i], heights[j])

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

            maxW = max(maxW, w)

        return maxW