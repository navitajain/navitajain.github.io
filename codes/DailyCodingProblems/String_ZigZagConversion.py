'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I 
'''

def convert(s, numRows):
    if not s:
        return ''
    
    if numRows == 1:
        return s
    
    if len(s) < numRows:
        return s
        
    rowS = {}   #dictionary to hold row keys and substring for the resp row
    # flag/trigger to set increasing or decreasing ptrs for the rows
    ptr, trigger =0,0
    
    for c in s:
        #not in rowS dict
        if ptr not in rowS:
            rowS[ptr] = c
        else:
            rowS[ptr] += c

        # set incremental or decremental trigger for ptr
        if ptr == 0:
            trigger = 0
        elif ptr == numRows-1:
            trigger = 1

        # perform ptr or row increment or decrement        
        if trigger == 0:
            ptr += 1
        elif trigger == 1:
            ptr -= 1

    print(rowS)        
    newS = ''
    # put together all rows 
    for i in range(numRows):
        newS += rowS[i]
    return newS
    
    
print(convert("AB",numRows=1))
    
    