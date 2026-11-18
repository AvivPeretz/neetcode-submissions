class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for n in nums:
            if (n-1) not in s:
                length = 0
                while (n + length) in s:
                    length += 1
                max_len = max(max_len,length)
        
        return max_len

'''
naive sol:
sort -> O(nlogn)
return len(longest_consecutive_sub_array)


nums = [2,20,4,10,3,4,5]
    []

'''