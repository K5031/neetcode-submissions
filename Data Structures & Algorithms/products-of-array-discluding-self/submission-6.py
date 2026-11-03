class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        right = 1

        #left
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        #right
        for i in range(n - 1, -1, -1):
            res[i] = right * res[i]
            right = right * nums[i]
        
        return res