# @Author: Hanyang
# @Date: 2020-10-28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def flipMatchVoyage(self, root, voyage):
    self.ans = []
    self.voyage = voyage
    self.step = 0
    self.can = True
    self.dfs(root)
    if not self.can:
      return [-1]
    return self.ans
  
  def dfs(self, root):
    # 终止条件
    if not self.can or not root:
      return
    if root.val == self.voyage[self.step]:
      self.step += 1
      if root.left and root.left.val == self.voyage[self.step]:
        self.dfs(root.left)
        self.dfs(root.right)
      elif root.right and root.right.val == self.voyage[self.step]:
        if root.left:
          self.ans.append(root.val)
        self.dfs(root.right)
        self.dfs(root.left)
      elif root.left or root.right:
        self.can = False
    else:
      self.can = False
    


if __name__ == "__main__":
  s = Solution()
