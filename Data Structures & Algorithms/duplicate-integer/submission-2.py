class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else: 
                seen.add(i)
        return False
    



'''
Psudo:
1. iterate the array from i = 0 to n 
2. if nums[i] was never seen before, mark it as seen
3. else, return true
4. if the iteration is complete, return false.

Naive:
seen = []
for i in size(nums):
    if nums[i] in seen return true
    else add nums[i] to seen
return false
Time: O(n)
Space: O(n)
'''   