class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        return [n for n,f in freqs.most_common(k)]
        
        