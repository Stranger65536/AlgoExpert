#
# Zigzag Traverse
# Write a function that takes in an n x m two-dimensional array
# (that can be square-shaped when n === m) and returns a one-dimensional
# array of all the array's elements in zigzag order.
#
# Zigzag order starts at the top left corner of the two-dimensional
# array, goes down by one element, and proceeds in a zigzag pattern
# all the way to the bottom right corner.
#
# Sample Input
# array = [
#   [1, 3, 4, 10],
#   [2, 5, 9, 11],
#   [6, 8, 12, 15],
#   [7, 13, 14, 16],
# ]
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Hints
# Hint 1
# Don't overthink this question by trying to come up with a clever way
# of getting the zigzag order. Think about the simplest checks that need
# to be made to decide when and how to change direction throughout the
# zigzag traversal.
#
# Hint 2
# Starting at the top left corner, iterate through the two-dimensional
# array by keeping track of the direction that you're moving in (up or
# down). If you're moving up, you know that you need to move in an
# up-right pattern and that you need to handle the case where you hit
# the top or the right borders of the array. If you're moving down, you
# know that you need to move in a down-left pattern and that you need to
# handle the case where you hit the left or the bottom borders of the
# array.
#
# Hint 3
# When going up, if you hit the right border, you'll have to go down
# one element; if you hit the top border, you'll have to go right one
# element. Similarly, when going down, if you hit the left border,
# you'll have to go down one element; if you hit the bottom border,
# you'll have to go right one element.
#
# Optimal Space & Time Complexity
# O(n) time | O(n) space - where n is the total number of elements in
# the two-dimensional array


def zigzagTraverse(array):
    # Write your code here.
    if len(array) < 1 or len(array[0]) < 1:
        return []
    n = len(array)
    m = len(array[0])
    if n == 1:
        return array[0]
    if m == 1:
        return [array[i][0] for i in range(n)]
    i = 0
    j = 0
    result = []
    d = 0
    diag_right = True
    # 1 diag up right
    # 3 diag down left

    size = n * m
    result.append(array[i][j])
    i += 1
    d = 1
    while len(result) < size:
        result.append(array[i][j])
        if diag_right:
            if i - 1 >= 0 and j + 1 < m:
                i -= 1
                j += 1
            elif j + 1 < m:
                diag_right = False
                j += 1
            else:
                diag_right = False
                i += 1
        else:
            if i + 1 < n and j - 1 >= 0:
                i += 1
                j -= 1
            elif i + 1 < n:
                diag_right = True
                i += 1
            else:
                diag_right = True
                j += 1

    return result
