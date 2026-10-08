class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        num_set = set()

        for i in nums:
            if i  in num_set:
                return i
            else:
                num_set.add(i)