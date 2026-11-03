class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        bestN = 0

        for i in s:
            if i-1 in s:
                continue
            else:
                n = 1
                while i+1 in s:
                    n += 1
                    i += 1
                if n > bestN:
                    bestN = n
        
        return bestN
