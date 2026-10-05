class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        i,n = 0, len(s)
        while i < n :
            s[i], s[n-1] = s[n-1], s[i]
            i += 1
            n -= 1