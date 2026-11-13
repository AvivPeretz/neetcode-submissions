class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        l1 = freqs.most_common(k)
        l2 = []
        for n,f in l1:
            l2.append(n)
        return l2
            
        
        
        
            

'''
Create a Counter dict of nums:



'''
        