class Solution:
    def firstMissingPositive(self, nums):
    	nums.sort()
    	first=0
    	for i in range(len(nums)):
    		if (nums[i]<=0 or (nums[i]==nums[i-1] and i!=0)):
    			continue
    		else:
    			first+=1
    			if nums[i]!=first:
    				return first

    	return first+1


def main():
	s=Solution()
	print(s.firstMissingPositive([1,2,0]))
	print(s.firstMissingPositive([3,4,-1,1]))
	print(s.firstMissingPositive([7,8,9,11,12]))
	print(s.firstMissingPositive([1,0,2,2,1]))
	print(s.firstMissingPositive([1]))

main()