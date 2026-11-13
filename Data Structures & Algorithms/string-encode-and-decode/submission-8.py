class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        ans = []
        for s in strs:
            t = len(s)
            ans.append(str(t))
            ans.append('#') #delimiter
            ans.append(s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            start = i

            while s[i] != '#':
                i+=1
            
            length = int(s[start:i])
            i+=1
            res.append(s[i:i+length])
            i += length
        
        return res

'''
len = 5
i=2
5#Hello5#World
       i     
s
0123456
'''
            