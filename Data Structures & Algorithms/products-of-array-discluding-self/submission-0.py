class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product from left
        prev_product = 1
        prev_val = 1
        l2r = [1] * len(nums)
        r2l = [1] * len(nums)

        for i in range(len(nums)):
            l2r[i] = prev_product
            prev_val = nums[i]
            prev_product = prev_val * prev_product

            # print(l2r[i])
            

        # from right    
        next_prod = 1
        next_val = 1
        prod_except_me = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            r2l[i] = next_prod
            next_val = nums[i]
            next_prod = next_val * next_prod
            
            prod_except_me[i] = r2l[i] * l2r[i]
            # print(r2l[i])
            
        return prod_except_me

        
