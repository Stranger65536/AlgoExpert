#
# Monotonic Array
# Write a function that takes in an array of integers and returns a
# boolean representing whether the array is monotonic.
#
# An array is said to be monotonic if its elements, from left to right,
# are entirely non-increasing or entirely non-decreasing.
#
# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Sample Output
# true
# Hints
# Hint 1
# You can solve this question by iterating through the input array from
# left to right once.
#
# Hint 2
# Try iterating through the input array from left to right, in search
# of two adjacent integers that can indicate whether the array is
# trending upward or downward. Once you've found the tentative trend
# of the array, at each element thereafter, compare the element to the
# previous one; if this comparison breaks the previously identified
# trend, the array isn't monotonic.
#
# Hint 3
# Alternatively, you can start by assuming that the array is both
# entirely non-decreasing and entirely non-increasing. As you iterate
# through each element, perform a check to see if you can invalidate
# one or both of your assumptions.
#
# Optimal Space & Time Complexity
# O(n) time | O(1) space - where n is the length of the array

def isMonotonic(array):
    # Write your code here.
    if len(array) < 2:
        return True
    dec = False
    inc = False
    for i in range(len(array) - 1):
        f1 = array[i]
        f2 = array[i + 1]
        if dec:
            if f2 > f1:
                return False
        elif inc:
            if f1 > f2:
                return False
        else:
            if f2 > f1:
                inc = True
            elif f1 > f2:
                dec = True
    return True
