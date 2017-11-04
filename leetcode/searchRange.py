class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return [-1, -1]
        
        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return [leftBound, rightBound]