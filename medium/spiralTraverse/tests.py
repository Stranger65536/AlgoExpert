# Add, edit, or remove tests in this file.
# Treat it as your playground!

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_2(self):
        matrix = [[1, 2], [4, 3]]
        expected = [1, 2, 3, 4]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_3(self):
        matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_4(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6],
                  [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                    16]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_5(self):
        matrix = [
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11],
        ]
        expected = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
        ]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_6(self):
        matrix = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [22, 23, 24, 25, 26, 27, 28, 29, 10],
            [21, 36, 35, 34, 33, 32, 31, 30, 11],
            [20, 19, 18, 17, 16, 15, 14, 13, 12],
        ]
        expected = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
        ]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_7(self):
        matrix = [
            [1, 2, 3, 4],
            [22, 23, 24, 5],
            [21, 36, 25, 6],
            [20, 35, 26, 7],
            [19, 34, 27, 8],
            [18, 33, 28, 9],
            [17, 32, 29, 10],
            [16, 31, 30, 11],
            [15, 14, 13, 12],
        ]
        expected = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
        ]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_8(self):
        matrix = [
            [1, 2, 3, 4],
            [10, 11, 12, 5],
            [9, 8, 7, 6],
        ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_9(self):
        matrix = [
            [1, 2, 3],
            [12, 13, 4],
            [11, 14, 5],
            [10, 15, 6],
            [9, 8, 7],
        ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(program.spiralTraverse(matrix), expected)
