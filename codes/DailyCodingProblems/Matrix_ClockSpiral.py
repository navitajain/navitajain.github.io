'''Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12'''

def clockSpiral(matrix):
    if len(matrix)==0 or len(matrix[0]) == 0:
           return
       
    row = len(matrix)
    col = len(matrix[0])
    
    #print col
    for i in range(col-1):
        print matrix[0][i]
    #print row
    for j in range(row):
        print matrix[j][col-1]
    
    #operation matrix[::-1][:-1] -> reverses the matrix and then omit the last row/list of the matrix
    cut_matrix = [r[:-1] for r in matrix[1:]]    
    
    #instead of traversing in clock spiral thr matrix, transform the matrix using list reversal and apply Recursion
    clockSpiral([r[::-1] for r in cut_matrix[::-1]])
    
    
    
    
# call function    
clockSpiral([[2,5],[8,4],[0,-1]])
    