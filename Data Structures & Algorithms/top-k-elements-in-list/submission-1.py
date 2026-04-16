class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_dict = {}

        
        for num in nums:
            count = count_dict.get(num, 0) + 1
            count_dict[num] = count
            

        sorted_items = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        ret_array = []
        for i in range(k):
            ret_array.append(sorted_items[i][0])

        return ret_array