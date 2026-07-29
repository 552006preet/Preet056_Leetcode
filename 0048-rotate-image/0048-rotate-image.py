class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #swapping the diagonal elements
        for i in range(n):  #rows 
            for j in range(i+1,n):  #colums
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]  #swapp
        
        for i in range(n): #reversing the rows
            matrix[i].reverse()
        return matrix