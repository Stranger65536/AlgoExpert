#
# Max Path Sum In Binary Tree
# Write a function that takes in a Binary Tree and returns its max
# path sum.
#
# A path is a collection of connected nodes in a tree where no node
# is connected to more than two other nodes; a path sum is the sum of
# the values of the nodes in a particular path.
#
# Each BinaryTree node has an integer value, a left child node, and a
# right child node. Children nodes can either be BinaryTree nodes
# themselves or None / null.
#
# Sample Input
# tree = 1
#     /     \
#    2       3
#  /   \   /   \
# 4     5 6     7
# Sample Output
# 18 // 5 + 2 + 1 + 3 + 7
# Hints
# Hint 1
# If you were to imagine each node in a Binary Tree as the root of
# the Binary Tree, temporarily eliminating all of the nodes that come
# above it, how would you find the max path sum for each of these newly
# imagined Binary Trees? In simpler terms, how can you find the max path
# sum for each subtree in the Binary Tree?
#
# Hint 2
# For every node in a Binary Tree, there are four options for the max
# path sum that includes its value: the node's value alone, the node's
# value plus the max path sum of its left subtree, the node's value plus
# the max path sum of its right subtree, or the node's value plus the
# max path sum of both its subtrees.
#
# Hint 3
# A recursive algorithm that computes each node's max path sum and uses
# it to compute its parents' nodes' max path sums seems appropriate, but
# realize that you cannot have a path going through a node and both its
# subtrees as well as that node's parent node. In other words, the
# fourth option mentioned in Hint #2 poses a challenge to implementing
# a recursive algorithm that solves this problem. How can you get around
# it?
#
# Optimal Space & Time Complexity
# O(n) time | O(log(n)) space - where n is the number of nodes in the
# Binary Tree


def maxPathSum(tree):
    def traverse(tree):
        if tree is None:
            return 0, 0
        left_max_b, left_max_p = traverse(tree.left)
        right_max_b, right_max_p = traverse(tree.right)
        max_child_sum_b = max(left_max_b, right_max_b)

        value = tree.value
        max_sum_b = max(max_child_sum_b + value, value)
        max_sum_root = max(left_max_b + value + right_max_b, max_sum_b)
        max_path_sum = max(left_max_p, right_max_p, max_sum_root)

        return max_sum_b, max_path_sum

    _, maxSum = traverse(tree)
    return maxSum
