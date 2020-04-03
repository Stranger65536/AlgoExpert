#
# Longest Peak
# Write a function that takes in an array of integers and returns
# the length of the longest peak in the array.
#
# A peak is defined as three or more adjacent integers in the array
# that are strictly increasing until they reach a tip (the highest value
# in the peak), at which point they become strictly decreasing.
#
# For example, the integers 1, 4, 10, 2 form a peak, but the integers
# 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly,
# the integers 1, 2, 3 don't form a peak because there aren't any
# strictly decreasing integers after the 3.
#
# Sample Input
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# Sample Output
# 6 // 0, 10, 6, 5, -1, -3
# Hints
# Hint 1
# You can solve this question by iterating through the array from
# left to right once.
#
# Hint 2
# Iterate through the array from left to right, and treat every
# integer as the potential tip of a peak. To be the tip of a peak,
# an integer has to be strictly greater than its adjacent integers.
# What can you do when you find an actual tip?
#
# Hint 3
# As you iterate through the array from left to right, whenever you
# find a tip of a peak, expand outwards from the tip until you no
# longer have a peak. Given what peaks look like and how many peaks
# can therefore fit in an array, realize that this process results
# in a linear-time algorithm. Make sure to keep track of the longest
# peak you find as you iterate through the array.
#
# Optimal Space & Time Complexity
# O(n) time | O(1) space - where n is the length of the input array


def longestPeak(array):
    # Write your code here.
    if len(array) < 3:
        return 0
    length = 0
    max_l = 0
    last = array[0]
    asc = False
    desc = False
    for i in range(1, len(array)):
        i = array[i]
        if i > last:
            if asc and desc:
                max_l = max(max_l, length)
                length = 2
                asc = True
                desc = False
            elif asc and not desc:
                length += 1
            elif not asc:
                length = 2
                asc = True
        elif i == last:
            if asc and desc:
                max_l = max(max_l, length)
                length = 0
                asc = False
                desc = False
            elif asc and not desc:
                length = 0
                asc = False
                desc = False
            elif not asc:
                length = 0
        elif i < last:
            if asc and desc:
                length += 1
            elif asc and not desc:
                length += 1
                desc = True
            elif not asc:
                length = 0
        last = i
    if desc:
        max_l = max(max_l, length)
    return max_l
