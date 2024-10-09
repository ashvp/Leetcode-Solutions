# 921. Minimum Add to Make Parentheses Valid
# Initially used Stack
# Stack is comparitively less efficient
# because the space complexity becomes O(n)
# whereas here, its O(1) since we use 
# constant variables.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = 0
        c = 0
        for i in s:
            if i == "(":
                o += 1
            else:
                if o > 0:
                    o -= 1
                else:
                    c += 1
        return o + c
    
