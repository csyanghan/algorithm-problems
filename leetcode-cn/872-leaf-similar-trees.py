# @Author: Hanyang
# @Date: 2020-10-30

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
      leaf1 = []
      leaf2 = []
      def dfs(root, leaf):
        if root == None: return
        if root.left == None and  root.right == None: 
            leaf.append(root.val)
            return
        dfs(root.left, leaf)
        dfs(root.right, leaf)
      
      dfs(root1,leaf1)
      dfs(root2, leaf2)

      return leaf1 == leaf2

if __name__ == "__main__":
  s = Solution()

