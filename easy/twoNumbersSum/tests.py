# Add, edit, or remove tests in this file.
# Treat it as your playground!

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = sorted(program.twoNumberSum([4, 6], 10))
        self.assertEqual(output, [4, 6])

    def test_case_2(self):
        output = sorted(program.twoNumberSum([4, 6, 1], 5))
        self.assertEqual(output, [1, 4])

    def test_case_3(self):
        output = sorted(program.twoNumberSum([4, 6, 1, -3], 3))
        self.assertEqual(output, [-3, 6])

    def test_case_4(self):
        output = sorted(
            program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual(output, [-1, 11])

    def test_case_5(self):
        output = sorted(
            program.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
        self.assertEqual(output, [8, 9])

    def test_case_6(self):
        output = sorted(
            program.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
        self.assertEqual(output, [3, 15])

    def test_case_7(self):
        output = sorted(
            program.twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))
        self.assertEqual(output, [-5, 0])

    def test_case_8(self):
        output = sorted(program.twoNumberSum(
            [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163))
        self.assertEqual(output, [-47, 210])

    def test_case_9(self):
        output = sorted(program.twoNumberSum(
            [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
        self.assertEqual(output, [])

    def test_case_10(self):
        output = sorted(
            program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))
        self.assertEqual(output, [])
