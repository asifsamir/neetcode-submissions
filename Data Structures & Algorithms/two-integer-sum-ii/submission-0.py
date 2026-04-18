class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        unique_nums = set(numbers)

        indices_return = []
        for index, num in enumerate(numbers):
            to_get = target - num

            if to_get in unique_nums:
                r_ind = numbers.index(to_get, index+1)
                indices_return.extend([index+1, r_ind+1])

                return indices_return

