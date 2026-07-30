class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left,ryt=0,len(matrix[0])-1
        top,bottom=0,len(matrix)-1
        ans=[]
        while left<=ryt and top<=bottom:
            for i in range(left,ryt+1):
                ans.append(matrix[top][i])
            top+=1
            if top<=bottom:
                for j in range(top,bottom+1):
                    ans.append(matrix[j][ryt])
                ryt-=1
            if left<=ryt and top<=bottom:
                for k in range(ryt,left-1,-1):
                    ans.append(matrix[bottom][k])
                bottom-=1
            if top<=bottom and left<=ryt:
                for l in range(bottom,top-1,-1):
                    ans.append(matrix[l][left])
                left+=1
        return ans