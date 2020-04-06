#
# BST Construction
# Write a BST class for a Binary Search Tree. The class should support:
#
# - Inserting values with the insert method.
# - Removing values with the remove method; this method should only
# remove the first instance of a given value.
# - Searching for values with the contains method.
# Note that you can't remove values from a single-node tree. In other
# words, calling the remove method on a single-node tree should simply
# not do anything.
#
# Each BST node has an integer value, a left child node, and a right
# child node. A node is said to be a valid BST node if and only if it
# satisfies the BST property: its value is strictly greater than the
# values of every node to its left; its value is less than or equal to
# the values of every node to its right; and its children nodes are
# either valid BST nodes themselves or None / null.
#
# Sample Usage
# // Assume the following BST has already been created:
#          10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
#
# // All operations below are performed sequentially.
# insert(12):   10
#             /     \
#            5      15
#          /   \   /   \
#         2     5 13   22
#       /        /  \
#      1        12  14
#
# remove(10):   12
#             /     \
#            5      15
#          /   \   /   \
#         2     5 13   22
#       /           \
#      1            14
#
# contains(15): true
# Hints
# Hint 1
# As you try to insert, find, or a remove a value into, in, or from
# a BST, you will have to traverse the tree's nodes. The BST property
# allows you to eliminate half of the remaining tree at each node that
# you traverse: if the target value is strictly smaller than a node's
# value, then it must be (or can only be) located to the left of the
# node, otherwise it must be (or can only be) to the right of that node.
#
# Hint 2
# Traverse the BST all the while applying the logic described in Hint
# #1. For insertion, add the target value to the BST once you reach a
# leaf (None / null) node. For searching, if you reach a leaf node
# without having found the target value that means the value isn't
# in the BST. For removal, consider the various cases that you might
# encounter: the node you need to remove might have two children nodes,
# one, or none; it might also be the root node; make sure to account
# for all of these cases.
#
# Hint 3
# What are the advantages and disadvantages of implementing these
# methods iteratively as opposed to recursively?
#
# Optimal Space & Time Complexity
# Average (all 3 methods): O(log(n)) time | O(1) space - where n is the
# number of nodes in the BST
# Worst (all 3 methods): O(n) time | O(1) space - where n is the number
# of nodes in the BST


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    node.left = BST(value)
                    return self
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BST(value)
                    return self
        return self

    def contains(self, value):
        node = self
        while node:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    return False
            elif node.value < value:
                if node.right:
                    node = node.right
                else:
                    return False
            else:
                return True
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        target_node = None
        parent = None
        while node:
            if node.value > value:
                if node.left:
                    parent = node
                    node = node.left
                else:
                    return self
            elif node.value < value:
                if node.right:
                    parent = node
                    node = node.right
                else:
                    return self
            else:
                target_node = node
                break
        if not target_node.left \
                and not target_node.right \
                and not parent:
            return self
        elif not target_node.left \
                and not target_node.right \
                and parent:
            if parent.left == target_node:
                parent.left = None
            else:
                parent.right = None
            return self
        elif target_node.left \
                and not target_node.right \
                and parent:
            if parent.left == target_node:
                parent.left = target_node.left
            else:
                parent.right = target_node.left
            return self
        elif target_node.right \
                and not target_node.left \
                and parent:
            if parent.left == target_node:
                parent.left = target_node.right
            else:
                parent.right = target_node.right
            return self
        elif target_node.right \
                and not target_node.left \
                and not parent:
            return target_node.right
        elif target_node.left \
                and not target_node.right \
                and not parent:
            return target_node.left
        elif target_node.right \
                and target_node.left \
                and not parent:
            cur_node = target_node
            cur_parent = target_node
            while True:
                if cur_node.left:
                    cur_parent = cur_node
                    cur_node = cur_node.left
                else:
                    break
            target_node.value = cur_node.value
            cur_parent.left = cur_node.right
            return self
        else:
            cur_node = target_node.right
            cur_parent = target_node
            while True:
                if cur_node.left:
                    cur_parent = cur_node
                    cur_node = cur_node.left
                else:
                    break
            target_node.value = cur_node.value
            cur_parent.left = cur_node.right
            return self
