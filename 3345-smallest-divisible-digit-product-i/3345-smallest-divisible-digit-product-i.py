class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(x:int)->int:
            product=1
            for i in str(x):
                product*=int(i)
            return product
        while True:
            if prod(n)%t==0:
                return n
            n+=1
            