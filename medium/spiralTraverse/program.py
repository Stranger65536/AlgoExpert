#
# Spiral Traverse
# Write a function that takes in an n x m two-dimensional array (that
# can be square-shaped when n === m) and returns a one-dimensional array
# of all the array's elements in spiral order.
#
# Spiral order starts at the top left corner of the two-dimensional
# array, goes to the right, and proceeds in a spiral pattern all the
# way until every element has been visited.
#
# Sample Input
# array = [
#   [1, 2, 3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10, 9, 8, 7],
# ]
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Hints
# Hint 1
# You can think of the spiral that you have to traverse as a set of
# rectangle perimeters that progressively get smaller (i.e., that
# progressively move inwards in the two-dimensional array).
#
# Hint 2
# Going off of Hint #1, declare four variables: a starting row, a
# starting column, an ending row, and an ending column. These four
# variables represent the bounds of the first rectangle perimeter in
# the spiral that you have to traverse. Traverse that perimeter using
# those bounds, and then move the bounds inwards. End your algorithm
# once the starting row passes the ending row or the starting column
# passes the ending column.
#
# Hint 3
# You can solve this problem both iteratively and recursively following
# very similar logic.
#
# Optimal Space & Time Complexity
# O(n) time | O(n) space - where n is the total number of elements in
# the array


def spiralTraverse(matrix):
    # Write your code here.
    def spiral(matrix, ib, ie, jb, je, result):
        if ib == ie and jb == je:
            result.append(matrix[ib][jb])
            return
        if ib == ie:
            for i in range(je - jb + 1):
                result.append(matrix[ib][jb + i])
            return
        if jb == je:
            for i in range(ie - ib + 1):
                result.append(matrix[ib + i][je])
            return
        for i in range(je - jb + 1):
            result.append(matrix[ib][jb + i])
        for i in range(ie - ib - 1):
            result.append(matrix[ib + i + 1][je])
        for i in range(je - jb + 1):
            result.append(matrix[ie][je - i])
        for i in range(ie - ib - 1):
            result.append(matrix[ie - i - 1][jb])

    if len(matrix) < 1:
        return
    if len(matrix[0]) < 1:
        return
    ib = 0
    jb = 0
    ie = len(matrix) - 1
    je = len(matrix[0]) - 1

    result = []
    while ib <= ie and jb <= je:
        spiral(matrix, ib, ie, jb, je, result)
        ib += 1
        ie -= 1
        jb += 1
        je -= 1

    return result
