class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m*n-1
        
        while left<=right:
            mid=left+(right-left)//2
        
            mid_value=matrix[mid//m][mid%m] #method to map 1-d index(mid) into 2-d matrix
        
            if mid_value==target:
                return True
            elif mid_value<target:
                left=mid+1
            else:
                right=mid-1
        return False
                
# either use above or make a function of binary search and search the element as method if binary search then use that function inside SEARCH-MATRIC function and only check the condition

# # def binarysrch(self,matrix:list[int],target:int)->int:
    #     left,right=0,len(matrix)-1
    #     while left<=right:
    #         mid=left+(right-left)
    #         if matrix[mid]==target:
    #             return mid
    #         elif matrix[mid]>target:
    #             right=mid-1
    #         else:
    #             left=mid+1
    #     return left