class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        h = []
        for (i, f) in freq.items():
            heapq.heappush(h, (-f, i))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res