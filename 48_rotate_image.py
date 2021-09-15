class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
    def reflect(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] =  matrix[i][-j-1], matrix[i][j]
                
    def transpose(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
board = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Solution().rotate(board)
print (board)