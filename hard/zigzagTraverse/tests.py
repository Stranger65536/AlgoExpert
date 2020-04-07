# Add, edit, or remove tests in this file.
# Treat it as your playground!

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1]]
        self.assertEqual(program.zigzagTraverse(test), [1])

    def test_case_2(self):
        test = [[1, 2, 3, 4, 5]]
        self.assertEqual(program.zigzagTraverse(test), [1, 2, 3, 4, 5])

    def test_case_3(self):
        test = [[1], [2], [3], [4], [5]]
        self.assertEqual(program.zigzagTraverse(test), [1, 2, 3, 4, 5])

    def test_case_4(self):
        test = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
        self.assertEqual(program.zigzagTraverse(test),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_case_5(self):
        test = [[1, 3, 4, 7, 8], [2, 5, 6, 9, 10]]
        self.assertEqual(program.zigzagTraverse(test),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_case_6(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15],
                [7, 13, 14, 16]]
        self.assertEqual(program.zigzagTraverse(test),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                          15, 16])

    def test_case_7(self):
        test = [[1, 3, 4, 10, 11], [2, 5, 9, 12, 19],
                [6, 8, 13, 18, 20], [7, 14, 17, 21, 24],
                [15, 16, 22, 23, 25]]
        self.assertEqual(
            program.zigzagTraverse(test),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 20, 21, 22, 23, 24, 25],
        )

    def test_case_8(self):
        test = [
            [1, 3, 4, 10, 11, 20],
            [2, 5, 9, 12, 19, 21],
            [6, 8, 13, 18, 22, 27],
            [7, 14, 17, 23, 26, 28],
            [15, 16, 24, 25, 29, 30],
        ]
        self.assertEqual(
            program.zigzagTraverse(test),
            [
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
            ],
        )

    def test_case_9(self):
        test = [
            [1, 3, 4, 10, 11],
            [2, 5, 9, 12, 20],
            [6, 8, 13, 19, 21],
            [7, 14, 18, 22, 27],
            [15, 17, 23, 26, 28],
            [16, 24, 25, 29, 30],
        ]
        self.assertEqual(
            program.zigzagTraverse(test),
            [
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
            ],
        )
