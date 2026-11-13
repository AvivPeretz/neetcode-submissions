class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        if s_list == t_list: return True
        return False




'''
Naive:
turn each string to a list, sort the list then compare them. 
if they match, return true, else return false.
Time: O(nlog(n)) -> create the array then sorting it (best is nlogn)
Space: O(n) -> array


'''

