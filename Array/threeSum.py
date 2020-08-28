# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res      


# exceeds time limit, but does the job.
# class Solution:
#     def threeSum(self, nums):
#         result=[]
#         for i, num in enumerate(nums):
#             complement = -num
#             new_list=nums[:i]+nums[i+1:]
#             for j,n in enumerate(new_list):
#             	flag=0
#                 required=complement-n
#                 for each in result:
#                     if set([num,n,required])==set(each):
#                         flag=1
#                         break
#                 if flag==1:
#                     continue
#                 elif required in new_list and new_list.index(required)!=j:
#                     result.append([num,n,required])
	    
# 	return result

def main():
    solution=Solution()
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    result = solution.threeSum(nums)
    print(result)
    
if __name__=="__main__":
    main()