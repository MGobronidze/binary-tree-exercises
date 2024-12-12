# Python Program to Check if Root to leaf path 
# sum equal to a given number 

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Check if there's a root-to-leaf path with
# the given sum
def hasPathSum(root, targetSum):
    if root is None:
        return False
    
    stack = []
    sums = []
    stack.append(root)
    sums.append(root.data)
    
    while stack:
        node = stack.pop()
        sumValue = sums.pop()
        
        # Check if leaf node and sum matches
        if node.left is None and node.right is None \
        and sumValue == targetSum:
            return True
        
        # Add children to stacks with updated sums
        if node.left:
            stack.append(node.left)
            sums.append(sumValue + node.left.data)
        if node.right:
            stack.append(node.right)
            sums.append(sumValue + node.right.data)
    
    return False

if __name__ == "__main__":
  
    # Construct binary tree
    #         10
    #       /  \
    #      8    2
    #     / \   /
    #    3   5 2
    
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
   
    targetSum = 21
    
    print(hasPathSum(root, targetSum))