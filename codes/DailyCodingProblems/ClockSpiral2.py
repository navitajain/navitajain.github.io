'''Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # single col to list 
        if len(matrix[0]) ==1:
            return [m[0] for m in matrix]
        
        #recurse
        return self.clockSpiral(matrix,[])
        
    def clockSpiral(self,matrix,l):
        if len(matrix)==0 or len(matrix[0]) == 0:
            return l
    
        row = len(matrix)
        col = len(matrix[0])
    
        # col
        for i in range(col-1):
            l.append(matrix[0][i])
        # row
        for j in range(row):
            l.append(matrix[j][col-1])
            
        #operation matrix[::-1][:-1] -> reverses the matrix and then omit the last row/list of the matrix
        cut_matrix = [r[:-1] for r in matrix[1:]]    
        #instead of traversing in clock spiral thr matrix, transform the matrix using list reversal and apply Recursion
        return self.clockSpiral([r[::-1] for r in cut_matrix[::-1]],l)
    
    
a = Solution()
print a.spiralOrder([[2,5],[8,4],[0,-1]])
print a.spiralOrder([[3],
             [2]])