class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #If the i, j element of A is denoted A_ij then we have
        #A_ij = A_(i+1,j+1) = a_(i-j), A Toeplitz matrix is not necessarily square.
        
        import numpy as np
        np_mat = np.array(matrix)
        
        isTMat = True
        
        #first row elements
        for count in range(len(np_mat[0])):
            isTMat = isTMat and self.checksDiagonal(np_mat, 0, count)
        
        #now for every first element in each row starting from second
        
        if not isTMat: #if already false here, no need to go further down
            return isTMat
        else:
            currentRow = 1
            while currentRow < len(np_mat):
                isTMat = isTMat and self.checksDiagonal(np_mat, currentRow, 0)
                if not isTMat: return isTMat
                currentRow += 1
        return isTMat
        
    def checksDiagonal(self, matrix, row, col):
        max_row = len(matrix)-1
        max_col = len(matrix[0])-1
        
        isEqualDiag = True
        
        while row < max_row and col < max_col:
            #print(row, col)
            isEqualDiag = isEqualDiag and (matrix[row,col] == matrix[row+1, col+1])
            row += 1
            col += 1
        return isEqualDiag