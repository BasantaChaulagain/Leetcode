class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=0
        for i in range(len(nums)-1,0,-1):
            # Find the first pair from right that is out of order, ie: inascending order
            # here nums[i-1] is the breaking point, which doesn't follow the order.
            if nums[i-1]<nums[i]:
                # Lists of all elements that is greater than breaking point
                max_list=[x for x in nums[i:] if x>nums[i-1]]
                
                # Minumum value in the max_list, to swap with the breaking point.
                # to_swap is the next value that is greater than breaking point.
                to_swap=min(max_list)
                
                # Swap breaking point value with to_swap.
                sw_ind=nums[i:].index(to_swap)+i
                nums[i-1],nums[sw_ind]=to_swap,nums[i-1]
                
                # Sort all the elements right to the breaking point. 
                nums[i:] = sorted(nums[i:])
                print(nums)

                flag=1
                break
        
        if flag==0:
            nums.sort()
            print(nums)

def main():
    s=Solution()
    s.nextPermutation([2,1,2,2,2,2,2,1])

main()