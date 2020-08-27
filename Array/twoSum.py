# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n1 in enumerate(nums):
            required = target-n1
            if required in nums and nums.index(required)!=i:
                return [i, nums.index(required)]

def main():
    solution=Solution()
    nums = [3,2,4]
    target = 6
    solution.twoSum(nums, target)
    
if __name__=="__main__":
    main()