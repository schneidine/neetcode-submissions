from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        best = 0 

        for num in nums_set:
            if num - 1 in nums_set:
                continue  # not the start of a sequence

            length = 1 
            while num+length in nums_set:
                length += 1

            best = max(best, length)

        return best
    
    
    # my horrible solution attempts
    #def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     count = 0 
    #     nums_set = set(nums)
    #     target = 0
        
    #     for num in nums:
    #         target = num-1

    #         if target in nums_set:
    #             continue
            
    #         while target not in nums_set:
    #             target = target + 1
               
    #             if target in nums_set:
    #                 count+=1
            
            
    #     return count+1


        