class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        self.ret = []
        
        def get_parenthesis(s, l, r):
            # l denotes the number of "(" left
            # r denotes the number of ")" left
            # l should always be less than r
            if l == 0:
                while r > 0:
                    s += ')'
                    r -= 1
                self.ret.append(s) 
                
            elif l == r:
                s += '('
                get_parenthesis(s, l-1, r)
                
            elif l < r:
                s += '('
                get_parenthesis(s, l-1, r)
                s = s[:-1]
                
                s += ')'
                get_parenthesis(s, l, r-1)
            else:
                return None                        
            
        get_parenthesis("", n, n)
        return self.ret
        

s = Solution()
a = s.generateParenthesis(1)
print(a)