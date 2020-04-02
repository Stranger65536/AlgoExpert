#
# Find Three Largest Numbers
# Write a function that takes in an array of integers and returns a
# sorted array of the three largest integers in the input array.
#
# The function should return duplicate integers if necessary; for
# example, it should return [10, 10, 12] for an input array of
# [10, 5, 9, 10, 12].
#
# Sample Input
# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# Sample Output
# [18, 141, 541]
# Hints
# Hint 1
# Can you keep track of the three largest numbers in an array as you
# traverse the input array?
#
# Hint 2
# Following the suggestion in Hint #1, try traversing the input array
# and updating the three largest numbers if necessary by shifting them
# accordingly.
#
# Optimal Space & Time Complexity
# O(n) time | O(1) space - where n is the length of the input array


def findThreeLargestNumbers(array):
    # Write your code here.
    f1 = None
    f2 = None
    f3 = None
    for i in array:
        if f1 is None:
            f1 = i
        elif f2 is None:
            if i < f1:
                f2 = f1
                f1 = i
            else:
                f2 = i
        elif f3 is None:
            if i < f2:
                if i < f1:
                    f3 = f2
                    f2 = f1
                    f1 = i
                else:
                    f3 = f2
                    f2 = i
            else:
                f3 = i
        else:
            if i > f1:
                if i > f2:
                    if i > f3:
                        f1 = f2
                        f2 = f3
                        f3 = i
                    else:
                        f1 = f2
                        f2 = i
                else:
                    f1 = i

    if f1 is None:
        return []
    if f2 is None:
        return [f1, f1, f1]
    if f3 is None:
        return [f1, f1, f2]
    return [f1, f2, f3]
