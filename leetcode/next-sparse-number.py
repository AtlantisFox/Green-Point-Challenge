# A number is Sparse if there are no two adjacent 1s in its binary representation.
# Given a number n, find the smallest Sparse number which greater than or equal to n.
# eg. 5 (binary representation: 101) is sparse, but 6 (binary representation: 110) is not sparse.
 
# Example
# Given n = 6, return 8
# Next Sparse Number is 8
 
# Given n = 4, return 4
# Next Sparse Number is 4
 
# Given n = 38, return 40
# Next Sparse Number is 40
 
# Given n = 44, return 64
# Next Sparse Number is 64
 
# idea:
#  	<------
# 01010001011101
#  	||
# 01010001100000
#  	||
# 01010010000000 

class Solution:
    """
    @param: : a number
    @return: return the next sparse number behind x
    """

    def nextSparseNum(self, x):
        binx = reversed(bin(x)[2:])
        list_binx = list(binx)
        last_final = 0
        for i in range(1, len(binx) - 1):
        	if list_binx[i] == '1' and list_binx[i-1] == '1' and list_binx[i+1] != '1':
        		list_binx[i+1] = '1';
        		for j in range(i, last_final, -1):
        			list_binx[j] = '0'
        		last_final = i + 1
        return int("".join(list_binx), 2)