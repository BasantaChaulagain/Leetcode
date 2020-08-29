class Solution:
    def searchRange(self, nums, target):
        try:
	        a=[i for i in range(len(nums)) if nums[i]==target]
	        return([a[0],a[-1]])
	    except:
	    	return [-1,-1]

		# first=last=-1
		# i=0
		# while i<len(nums):
		# 	if nums[i]==target:
		# 		if first==-1:
		# 			first=last=i
		# 		else:
		# 			last=i
		# 	i+=1
		# return[first,last]


nums=[1,2,2,3,3,3,3,3,3,3,4,5,6,7,8]
s=Solution()
result=s.searchRange(nums,3)
print(result)