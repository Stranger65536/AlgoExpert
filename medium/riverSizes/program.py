#
# River Sizes
# You're given a two-dimensional array (a matrix) of potentially unequal
# height and width containing only 0s and 1s. Each 0 represents land,
# and each 1 represents part of a river. A river consists of any number
# of 1s that are either horizontally or vertically adjacent (but not
# diagonally adjacent). The number of adjacent 1s forming a river
# determine its size.
#
# Write a function that returns an array of the sizes of all rivers
# represented in the input matrix. The sizes don't need to be in any
# particular order.
#
# Sample Input
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0],
# ]
# Sample Output
# [1, 2, 2, 2, 5] // the numbers could be ordered differently
# Hints
# Hint 1
# Since you must return the sizes of rivers, which consist of
# horizontally and vertically adjacent 1s in the input matrix,
# you must somehow keep track of groups of neighboring 1s as you
# traverse the matrix. Try treating the matrix as a graph, where
# each element in the matrix is a node in the graph with up to 4
# neighboring nodes (above, below, to the left, and to the right),
# and traverse it using a popular graph-traversal algorithm like
# Depth-first Search or Breadth-first Search.
#
# Hint 2
# By traversing the matrix using DFS or BFS as mentioned in Hint #1,
# any time that you encounter a 1 you can traverse the entire river
# that this 1 is a part of (and keep track of its size) by simply
# iterating through the given node's neighboring nodes and their own
# neighboring nodes so long as the nodes are 1s.
#
# Hint 3
# Naturally, many nodes in the graph mentioned in Hint #1 will have
# overlapping neighboring nodes, and as you traverse the matrix, you
# will undoubtedly encounter nodes that you have previously visited.
# In order to prevent mistakenly calculating the same river's size
# multiple times and to avoid doing needless computational work, try
# keeping track of every node that you visit in an auxiliary data
# structure and only performing important computations on unvisited
# nodes. What data structure would be ideal here?
#
# Optimal Space & Time Complexity
# O(wh) time | O(wh) space - where w and h are the width and height
# of the input matrix


def riverSizes(matrix):
    # Write your code here.
    n = len(matrix)
    if n < 1:
        return []
    m = len(matrix[0])
    visited = []
    for i in range(n):
        visited.append([0 for j in range(m)])
    result = []
    traversed = [0]

    def traverse(matrix, visited, i, j):
        if visited[i][j]:
            pass
        else:
            visited[i][j] = True
            traversed[0] += 1
        if i - 1 >= 0:
            if not visited[i - 1][j] and matrix[i - 1][j]:
                traverse(matrix, visited, i - 1, j)
        if i + 1 < n:
            if not visited[i + 1][j] and matrix[i + 1][j]:
                traverse(matrix, visited, i + 1, j)
        if j - 1 >= 0:
            if not visited[i][j - 1] and matrix[i][j - 1]:
                traverse(matrix, visited, i, j - 1)
        if j + 1 < m:
            if not visited[i][j + 1] and matrix[i][j + 1]:
                traverse(matrix, visited, i, j + 1)

    for i in range(n):
        for j in range(m):
            traversed[0] = 0
            if not visited[i][j] and matrix[i][j]:
                traverse(matrix, visited, i, j)
                result.append(traversed[0])

    return result
