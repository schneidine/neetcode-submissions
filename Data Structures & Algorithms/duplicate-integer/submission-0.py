class Solution:
    """"Using a dict/hash map, you can search for duplicates
        in O(n) since you dont have to check each number against
        each number O(n^2)"""
        
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dictionary
        num_dict = {}

        for val in nums:
            if val in num_dict:
                return True
            else:
                num_dict[val] = True
                
        return False




        

