from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                if level % 2 == 1: # Check if it's an odd level
                    current_level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse node values at odd levels
            if current_level_nodes:
                values = [node.val for node in current_level_nodes][::-1]
                for i in range(len(current_level_nodes)):
                    current_level_nodes[i].val = values[i]
            
            level += 1
        
        return root
