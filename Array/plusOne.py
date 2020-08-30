class Solution:
    def plusOne(self, digits):
        number=0
        for i in digits:
        	number=number*10+i
        digits=[]
        number+=1
        while number!=0:
        	digits.append(number%10)
        	number=number//10
        digits.reverse()
        return digits

s=Solution()
print(s.plusOne([4,3,2,9]))