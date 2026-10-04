class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i, n = 0, len(nums)
        while i < n:
            j = i + 1
            while  j < n :
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
            i += 1
    
        return [0,0]