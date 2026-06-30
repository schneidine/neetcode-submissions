class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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


