class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # calculate their frequencies
        freq = defaultdict(int)
       
       # find the frequencies
        for num in nums:
            freq[num] +=1
        
        heap = []

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


            





        
        


        