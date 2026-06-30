class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero= 0

        for i in nums:
            if i != 0:
                product *= i
            else: 
                count_zero+=1
        
        result = []

        if count_zero == len(nums) or count_zero>1:
            return [0]*len(nums)

        if count_zero == 1:
            for i in nums:
                if i == 0:
                    result.append(product)
                else:
                    result.append(0)
            return result

        for i in range(len(nums)):
            result.append(int(product/nums[i]))

        return result
        