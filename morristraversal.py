# Python program to see if two trees are identical
# using Morris Traversal
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to check if two trees are identical 
# using Morris traversal
def isIdentical(r1, r2):

    # Check if both trees are empty
    if r1 is None and r2 is None:
        return True

    # Check if one tree is empty and the other is not
    if r1 is None or r2 is None:
        return False

    # Morris traversal to compare both trees
    while r1 is not None and r2 is not None:

        # Compare the data of both current nodes
        if r1.data != r2.data:
            return False

        # Morris traversal for the first tree (r1)
        if r1.left is None:

            # Move to the right child if no left child
            r1 = r1.right
        else:

            # Find the inorder predecessor of r1
            pre = r1.left
            while pre.right is not None and pre.right != r1:
                pre = pre.right

            # Set the temporary link to r1
            if pre.right is None:
                pre.right = r1
                r1 = r1.left

            # Remove the temporary link and move to right
            else:
                pre.right = None
                r1 = r1.right

        # Morris traversal for the second tree (r2)
        if r2.left is None:

            # Move to the right child if no left child
            r2 = r2.right
        else:

            # Find the inorder predecessor of r2
            pre = r2.left
            while pre.right is not None and pre.right != r2:
                pre = pre.right

            # Set the temporary link to r2
            if pre.right is None:
                pre.right = r2
                r2 = r2.left

            # Remove the temporary link and move to right
            else:
                pre.right = None
                r2 = r2.right

    # Both trees are identical if both are null at end
    return r1 is None and r2 is None

if __name__ == '__main__':
  
    # Representation of input binary tree 1
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)

    # Representation of input binary tree 2
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(3)
    r2.left.left = Node(4)

    if isIdentical(r1, r2):
        print("Yes")
    else:
        print("No")