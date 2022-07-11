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

    
    
  """"
  
  return False if x < 0 else x == int(str(x)[::-1])

  
  """
