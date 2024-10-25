def solve(M, n):
    def determinant(matrix):
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) -
                matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2]) +
                matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]))

    def inverse(matrix):
        det = determinant(matrix)
        return [[(matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) / det,
                 (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) / det,
                 (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) / det],
                [(matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) / det,
                 (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) / det,
                 (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) / det],
                [(matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) / det,
                 (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) / det,
                 (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) / det]]

    inv_matrix = inverse(M)
    print(' '.join(map(str, map(int, inv_matrix[n-1]))))

