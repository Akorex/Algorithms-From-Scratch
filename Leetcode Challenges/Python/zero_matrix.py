"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0. 

"""
import unittest


def set_zero_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    temp_rows = [False] * rows
    temp_cols = [False] * cols

    # find the entry that is 0 & find a way to mark them
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                temp_rows[row] = True
                temp_cols[col] = True

    # set the desired locations to 0
    for row in range(rows):
        for col in range(cols):
            if temp_rows[row] or temp_cols[col]:
                matrix[row][col] = 0

    return matrix



class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    def test_set_zero_matrix(self):

        for (matrix, result) in self.test_cases:
            assert result ==set_zero_matrix(matrix)
    

if __name__ == '__main__':
    unittest.main()