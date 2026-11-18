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

Solution:
turn nums into a set for O(1) search queries
initiate the longest sequence to 0
for each number (n) in the original array:
    if n-1 not exists in the set, n is the a start of a sequence:
        then, initialize the current length of the sequence to 0
        while n + length exist in our set:
            increment length by 1
        then initialize the longest sequence to the max length 
then return the max length of the sequence

'''