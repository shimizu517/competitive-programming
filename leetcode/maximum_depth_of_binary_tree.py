from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  max_depth = 0
  def maxDepth(self, root: TreeNode) -> int:
    q = deque()
    q.append(root)
    depth = 0
    while True:
      s = q.popleft()
      if s.left:
        q.append(s.left)
      if s.right:
        q.append(s.right)
      depth += 1


class Solution2:
  max_depth = 0
  def maxDepth(self, root: TreeNode) -> int:
    if root:
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    else:
      return 0