class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, num in enumerate(nums):
            to_have = target-num
            for j_index in range(i_index+1, len(nums)):
                if nums[j_index]==to_have:
                    return [i_index, j_index]



