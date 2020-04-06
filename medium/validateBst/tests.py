# Add, edit, or remove tests in this file.
# Treat it as your playground!

import unittest

import program


class StartBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


progBST = StartBST
if hasattr(program, "BST"):
    progBST = program.BST


class BST(progBST):
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(
            1).insert(22).insert(13).insert(14)
        self.assertEqual(program.validateBst(test1), True)

    def test_case_2(self):
        test2 = (
            BST(10)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(-5)
                .insert(-15)
                .insert(-5)
                .insert(-2)
                .insert(-1)
                .insert(-22)
        )
        self.assertEqual(program.validateBst(test2), True)

    def test_case_3(self):
        test3 = BST(10)
        self.assertEqual(program.validateBst(test3), True)

    def test_case_4(self):
        test4 = (
            BST(10)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(500)
                .insert(1500)
                .insert(50)
                .insert(200)
                .insert(10000)
                .insert(2200)
        )
        self.assertEqual(program.validateBst(test4), True)

    def test_case_5(self):
        test5 = (
            BST(5000)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(1)
                .insert(1)
                .insert(3)
                .insert(1)
                .insert(1)
                .insert(502)
                .insert(55000)
                .insert(204)
                .insert(205)
                .insert(207)
                .insert(206)
                .insert(208)
                .insert(203)
        )
        self.assertEqual(program.validateBst(test5), True)

    def test_case_6(self):
        test6 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(
            1).insert(22)
        test6.left.right.right = BST(11)
        self.assertEqual(program.validateBst(test6), False)

    def test_case_7(self):
        test7 = (
            BST(10)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(-5)
                .insert(-15)
                .insert(-5)
                .insert(-2)
                .insert(-1)
                .insert(-22)
        )
        test7.left.left.left.left.left.left.left = BST(11)
        self.assertEqual(program.validateBst(test7), False)

    def test_case_8(self):
        test8 = BST(10).insert(12)
        test8.left = BST(11)
        self.assertEqual(program.validateBst(test8), False)

    def test_case_9(self):
        test9 = (
            BST(10)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(500)
                .insert(1500)
                .insert(50)
                .insert(200)
                .insert(10000)
                .insert(2200)
        )
        test9.right.right.right.right.right.right = BST(9999)
        self.assertEqual(program.validateBst(test9), False)

    def test_case_10(self):
        test10 = (
            BST(100)
                .insert(5)
                .insert(15)
                .insert(5)
                .insert(2)
                .insert(1)
                .insert(22)
                .insert(1)
                .insert(1)
                .insert(3)
                .insert(1)
                .insert(1)
                .insert(502)
                .insert(55000)
                .insert(204)
                .insert(205)
                .insert(207)
                .insert(206)
                .insert(208)
                .insert(203)
        )
        test10.right.left.right.left = BST(300)
        self.assertEqual(program.validateBst(test10), False)

    def test_case_11(self):
        test11 = BST(10).insert(5).insert(15)
        test11.left.right = BST(10)
        self.assertEqual(program.validateBst(test11), False)
