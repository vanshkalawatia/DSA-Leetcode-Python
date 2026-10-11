class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        num = list(str(x))

        num.reverse()

        if (list(str(x)) == num ):
            return True
        else:
            return False