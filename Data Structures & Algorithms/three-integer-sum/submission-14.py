class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            Li, Ri = i + 1, len(nums) - 1

            while Li < Ri:
                s = nums[i] + nums[Li] + nums[Ri]

                if s == 0:
                    ret.append([nums[i], nums[Li], nums[Ri]])

                    Li += 1
                    Ri -= 1

                    # skip duplicates
                    while Li < Ri and nums[Li] == nums[Li - 1]:
                        Li += 1
                    while Li < Ri and nums[Ri] == nums[Ri + 1]:
                        Ri -= 1

                elif s < 0:
                    Li += 1
                else:
                    Ri -= 1

        return ret