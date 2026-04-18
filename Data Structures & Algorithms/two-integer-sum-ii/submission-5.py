class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # unique_nums = set(numbers)

        # for index, num in enumerate(numbers):
        #     to_get = target - num

        #     if to_get in unique_nums:
        #         r_ind = numbers.index(to_get, index+1)
        #         return [index+1, r_ind+1]


        Li = 0
        Ri = len(numbers) - 1

        indices_return = []
        while Li < Ri:
            temp = numbers[Li] + numbers[Ri]

            if temp == target:
                return [Li+1, Ri+1]
            elif temp > target and Ri > -1:
                while temp > target:
                    Ri -= 1
                    temp = numbers[Li] + numbers[Ri]
            else:
                while temp < target and Li < len(numbers):
                    Li += 1
                    temp = numbers[Li] + numbers[Ri]



