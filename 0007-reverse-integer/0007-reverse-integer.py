class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if x > INT_MAX or x < INT_MIN :
            return 0
        sign = -1 if x < 0 else 1
        rev = 0
        num = abs(x)

        while num >0 :

            if rev > INT_MAX // 10 or rev < INT_MIN /10 :
                return 0
            rev = (rev *10) + (num % 10)
            num = num // 10


        return rev * sign