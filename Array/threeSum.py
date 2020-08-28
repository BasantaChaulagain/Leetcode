# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.


# exceeds time limit, but does the job.
class Solution:
    def threeSum(self, nums):
        result=[]
        for i, num in enumerate(nums):
            complement = -num
            new_list=nums[:i]+nums[i+1:]
            for j,n in enumerate(new_list):
            	flag=0
                required=complement-n
                for each in result:
                    if set([num,n,required])==set(each):
                        flag=1
                        break
                if flag==1:
                    continue
                elif required in new_list and new_list.index(required)!=j:
                    result.append([num,n,required])
	    
	return result

def main():
    solution=Solution()
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    result = solution.threeSum(nums)
    print(result)
    
if __name__=="__main__":
    main()