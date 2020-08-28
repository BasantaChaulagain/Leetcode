class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1


def main():
    solution=Solution()
    nums = [4,6,8,9,10,0,2,3]
    target = 8
    print(solution.search(nums, target))
    
if __name__=="__main__":
    main()