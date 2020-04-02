#
# Linked List Construction
# Write a DoublyLinkedList class that has a head and a tail, both of
# which point to either a linked list Node or None / null. The class
# should support:
#
# - Setting the head and tail of the linked list.
# - Inserting nodes before and after other nodes as well as at given
# positions.
# - Removing given nodes and removing nodes with given values;
# - Searching for nodes with given values.
# Each Node has an integer value as well as a prev node and a next node,
# both of which can point to either another node or None / null.
#
# Sample Usage
# // Assume the following linked list has already been created:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with
# value 4 as the head
# setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the existing node
# with value 6 as the tail
# insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the
# existing node with value 3 before the existing node with value 6
# insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a
# new node with value 3 after the existing node with value 6
# insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3
# // insert a new node with value 3 in position 1
# removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes
# with value 3
# remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing
# node with value 2
# containsNodeWithValue(5): true
# Hints
# Hint 1
# When dealing with linked lists, it's very important to keep track of
# pointers on nodes (i.e., the "next" and "prev" properties on the
# nodes). For instance, if you're inserting a node in a linked list,
# but that node is already located somewhere else in the linked list
# (in other words, if you're moving a node), it's crucial to completely
# update the pointers of the adjacent nodes of the node being moved
# before updating the node's own pointers. The order in which you update
# nodes' pointers will make or break your algorithm.
#
# Hint 2
# Realize that the insertBefore() and insertAfter() methods can be used
# to implement the setHead(), setTail(), and insertAtPosition() methods;
# making the insertBefore() and insertAfter() methods as robust as
# possible will simplify your code for the other methods. Make sure to
# take care of edge cases involving inserting nodes before the head of
# the linked list or inserting nodes after the tail of the linked list.
#
# Hint 3
# Similar to Hint #2, realize that the remove() method can be used to
# implement the removeNodesWithValue() method as well as parts of the
# insertBefore() and insertAfter() methods; make sure that the remove()
# method handles edge cases regarding the head and the tail.
#
# Optimal Space & Time Complexity
# setHead, setTail, insertBefore, insertAfter, and remove: O(1)
# time | O(1) space
# insertAtPosition: O(p) time | O(1) space - where p is input position
# removeNodesWithValue, containsNodeWithValue: O(n) time | O(1)
# space - where n is the number of nodes in the linked list


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if node == nodeToInsert:
            return

        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return

        self.remove(nodeToInsert)

        if node.prev:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
            node.prev = nodeToInsert
            nodeToInsert.next = node
        else:
            self.head = nodeToInsert
            nodeToInsert.prev = None
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if node == nodeToInsert:
            return

        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return

        self.remove(nodeToInsert)

        if node.next:
            node.next.prev = nodeToInsert
            nodeToInsert.prev = node
            nodeToInsert.next = node.next
            node.next = nodeToInsert
        else:
            self.tail = nodeToInsert
            nodeToInsert.next = None
            nodeToInsert.prev = node
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        node = self.head
        for i in range(position - 1):
            node = node.next if node else None
        if node is None:
            if position == 1:
                self.insertBefore(self.tail, nodeToInsert)
            else:
                self.insertAfter(self.tail, nodeToInsert)
        else:
            self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        if self.head is None:
            return
        node = self.head
        while node:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node
        return

    def remove(self, node):
        # Write your code here.
        if node.prev:
            node.prev.next = node.next
        elif node.next:
            self.head = node.next
        elif self.head == node:
            self.head = None
        if node.next:
            node.next.prev = node.prev
        elif node.prev:
            self.tail = node.prev
        elif self.tail == node:
            self.tail = None
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        if self.head is None:
            return False
        node = self.head
        if node.value == value:
            return True
        while node.next:
            node = node.next
            if node.value == value:
                return True
        return False
