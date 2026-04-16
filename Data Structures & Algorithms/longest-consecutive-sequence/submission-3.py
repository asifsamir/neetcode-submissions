class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_length = 0

        for num in numSet:
            # have to consider either starting from beginning of the series or end of the series
            # this example is for beginning of the series
            if num - 1 in numSet:
                continue
            else:
                length = 1
                temp_num = num
                
                while (temp_num + 1) in numSet:
                    length += 1
                    temp_num += 1


                if length > longest_length:
                    longest_length = length


        return longest_length