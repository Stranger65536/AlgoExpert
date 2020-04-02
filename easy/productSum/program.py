#
# Product Sum
# Write a function that takes in a "special" array and returns its
# product sum. A "special" array is a non-empty array that contains
# either integers or other "special" arrays. The product sum of a
# "special" array is the sum of its elements, where "special" arrays
# inside it are summed themselves and then multiplied by their level
# of depth.
#
# For example, the product sum of [x, y] is x + y; the product sum
# of [x, [y, z]] is x + 2y + 2z.
#
# Sample Input
# array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# Sample Output
# 12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2
# * (6 + 3 * (-13 + 8) + 4)
# Hints
# Hint 1
# Try using recursion to solve this problem.
#
# Hint 2
# Initialize the product sum of the "special" array to 0. Then,
# iterate through all of the array's elements; if you come across
# a number, add it to the product sum; if you come across another
# "special" array, recursively call the productSum function on it and
# add the returned value to the product sum. How will you handle
# multiplying the product sums at a given level of depth?
#
# Hint 3
# Have the productSum function take in a second parameter: the
# multiplier, initialized to 1. Whenever you recursively call the
# productSum function, pass in the multiplier incremented by 1.
#
# Optimal Space & Time Complexity
# O(n) time | O(d) space - where n is the total number of elements
# in the array, including sub-elements, and d is the greatest depth
# of "special" arrays in the array


def productSum(array):
    # Write your code here.
    def proc(arr, level):
        s = 0
        for i in arr:
            s += proc(i, level + 1) if isinstance(i, list) else i
        return level * s

    return proc(array, 1)
