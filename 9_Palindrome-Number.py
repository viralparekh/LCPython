"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        sp = 0
        lp = len(strx)-1
        while sp<lp:
            if strx[sp]==strx[lp]:
                sp += 1
                lp -= 1
            else:
                return False
        return True

    
    
## without converting to str

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        
        rev_digit = []
        temp = x
        while temp>0:
            digit = temp % 10
            rev_digit.append(digit)
            temp = temp //10
        
        return rev_digit==rev_digit[::-1]
            
    
  """"
  
  return False if x < 0 else x == int(str(x)[::-1])

  
  """
