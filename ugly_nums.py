#神奇的题解
n = int(input())

if n <= 6 :
    print(n)
else:
    res = [0 for i in range(n)]
    res[0] = 1
    a, b, c = 0, 0, 0
    
    for i in range(1,n):
        res[i] = min(res[a]*2,res[b]*3,res[c]*5)
        if(res[i]==res[a]*2): 
            a += 1
        if(res[i]==res[b]*3): 
            b += 1
        if(res[i]==res[c]*5): 
            c += 1
    print(res)
    print(res[n-1])


 #九章题解   
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([1])
        
        val = 0
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2,3,5]:
                res = val * factor
                if res not in visited:
                    heapq.heappush(heap, res)
                visited.add(res)
        return val    
