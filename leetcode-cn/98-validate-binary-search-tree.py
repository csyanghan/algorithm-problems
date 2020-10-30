# @Author: Hanyang
# @Date: 2020-10-30

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  pre = None
  def isValidBST(self, root: TreeNode) -> bool:
    if not root: return True
    if not self.isValidBST(root.left): return False
    if self.pre == None: self.pre = root
    elif root.val <= self.pre.val: return False
    self.pre = root
    return self.isValidBST(root.right)

if __name__ == "__main__":
  s = Solution()
