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
            heapq.heappush(h, (f, i))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for (f, i) in h:
            res.append(i)
        
        return res