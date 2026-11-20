class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #pairs of [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx)
            stack.append([t,i])
        return res
    
'''
Naive: O(n^2)

Solution:
initialize res array of zeros and and empty stack
the stack will store pairs of [temp,index]

while the stack is empty and the current temperature is greater than 
the top element temperature in the stack, pop the temp and index, calculate the difference between the indecies (days) and append it to the corresponding position of the result array
then, append a new pair of [temp,index] and keep going

we do not append 0's because the result array was initialized beforhand

Time: O(n)
'''