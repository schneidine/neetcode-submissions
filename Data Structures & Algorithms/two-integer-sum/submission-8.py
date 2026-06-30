class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Explanation - This solution makes use of a hashmap and stores each number and its index
        # Basically, you want to use subtraction from the target to find out what the 
        # number should be, and then do O(1) lookup to see if it exists in the hashmap.

        # add array to dictionary
        numbers = {}

        for i in range(len(nums)):
            numbers[nums[i]] = i 

        for num in range(len(nums)):
            answer = target - nums[num]
            print(f"{answer} and {nums[num]}")
            if answer in numbers and (numbers[answer] != num):
                if numbers[answer]<num:
                    return [numbers[answer],num]
                else:
                    return [num,numbers[answer]]
            else:
                continue


