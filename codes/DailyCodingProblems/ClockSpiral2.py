class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix[0]) ==1:
            return [m[0] for m in matrix]
        l = []
        return self.clockSpiral(matrix,l)
        
    def clockSpiral(self,matrix,l):
        if len(matrix)==0 or len(matrix[0]) == 0:
            return l
    
        row = len(matrix)
        col = len(matrix[0])
    
        # col
        for i in range(col-1):
            l.append(matrix[0][i])
        #print row
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