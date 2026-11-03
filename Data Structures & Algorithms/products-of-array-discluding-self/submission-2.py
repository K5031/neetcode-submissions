class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        left = [1] * n
        right = [1] * n

        #left
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        #right
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        for n in range(len(nums)):
            res.append(left[n] * right[n])

        return res