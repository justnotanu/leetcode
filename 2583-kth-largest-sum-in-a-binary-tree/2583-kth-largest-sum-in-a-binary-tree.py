# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        level_sums = []  # List to store sums of each level
        queue = deque([root])  # Queue for BFS
        
        # Perform BFS to calculate sums of each level
        while queue:
            level_sum = 0  # Initialize sum for the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val  # Add the value of the current node
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level_sums.append(level_sum)  # Store the sum of the current level
        
        # Sort sums in descending order
        level_sums.sort(reverse=True)
        
        # Return the kth largest sum or -1 if there are fewer than k levels
        return level_sums[k - 1] if k <= len(level_sums) else -1

    