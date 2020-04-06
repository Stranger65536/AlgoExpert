#
# Smallest Difference
# Write a function that takes in two non-empty arrays of integers,
# finds the pair of numbers (one from each array) whose absolute
# difference is closest to zero, and returns an array containing these
# two numbers, with the number from the first array in the first
# position.
#
# Assume that there will only be one pair of numbers with the smallest
# difference.
#
# Sample Input
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
# Sample Output
# [28, 26]
# Hints
# Hint 1
# Instead of generating all possible pairs of numbers, try somehow only
# looking at pairs that you know could actually have the smallest
# difference. How can you accomplish this?
#
# Hint 2
# Would it help if the two arrays were sorted? If the arrays were sorted
# and you were looking at a given pair of numbers, could you efficiently
# find the next pair of numbers to look at? What are the runtime
# implications of sorting the arrays?
#
# Hint 3
# Start by sorting both arrays, as per Hint #2. Put a pointer at the
# beginning of both arrays and evaluate the absolute difference of the
# pointer-numbers. If the difference is equal to zero, then you've found
# the closest pair; otherwise, increment the pointer of the smaller of
# the two numbers to find a potentially better pair. Continue until you
# get a pair with a difference of zero or until one of the pointers gets
# out of range of its array.
#
# Optimal Space & Time Complexity
# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the
# first input array and m is the length of the second input array


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    min_diff = None
    min_diff_1 = None
    min_diff_2 = None
    pointer1 = 0
    pointer2 = 0
    if not arrayOne or not arrayTwo:
        return 0
    while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
        e1 = arrayOne[pointer1]
        e2 = arrayTwo[pointer2]
        if e1 == e2:
            return [e1, e2]
        elif e1 < e2:
            if min_diff:
                if e2 - e1 < min_diff:
                    min_diff = e2 - e1
                    min_diff_1 = e1
                    min_diff_2 = e2
            else:
                min_diff = e2 - e1
                min_diff_1 = e1
                min_diff_2 = e2
            pointer1 += 1
        else:
            if min_diff:
                if e1 - e2 < min_diff:
                    min_diff = e1 - e2
                    min_diff_1 = e1
                    min_diff_2 = e2
            else:
                min_diff = e1 - e2
                min_diff_1 = e1
                min_diff_2 = e2
            pointer2 += 1
    return [min_diff_1, min_diff_2]
