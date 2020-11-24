# @Author: Hanyang
# @Date: 2020-11-24

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
      if not root: return 0
      res = 1
      if root.left: res += self.countNodes(root.left)
      if root.right: res += self.countNodes(root.right)
      return res

if __name__ == "__main__":
  s = Solution()
