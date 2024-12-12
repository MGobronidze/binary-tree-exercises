# Python program to find the height of a binary 
# tree using depth-first search (DFS) approach.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Returns height which is the number of edges
# along the longest path from the root node down 
# to the farthest leaf node.
def height(root):
    if root is None:
        return -1

    # compute the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight) + 1

if __name__ == "__main__":
  
    # Representation of the input tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(height(root))