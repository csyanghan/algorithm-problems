# @Author: Hanyang
# @Date: 2020-10-29

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
      if not root:
        return True
      return bool(self.height(root))

    def height(self, root: TreeNode):
      if not root:
        return 0
      if not root.left and not root.right:
        return 1
      left = self.height(root.left)
      if (type(left) == bool): return False
      right = self.height(root.right)
      if (type(right) == bool): return False
      if abs(right - left) > 1:
        return False
      return 1 + max(left, right)

if __name__ == "__main__":
  s = Solution()
