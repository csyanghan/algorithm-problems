# @Author: Hanyang
# @Date: 2020-11-18
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
      if len(preorder) == 0:
        return None
      head = TreeNode(preorder[0])
      index = inorder.index(preorder[0])
      left_tree_inorder = inorder[:index]
      right_tree_inorder = inorder[index+1:]
      left_tree_count = len(left_tree_inorder)
      right_tree_count = len(right_tree_inorder)
      left_tree_preorder = preorder[1:1+left_tree_count]
      right_tree_preorder = preorder[1+left_tree_count:]
      head.left = self.buildTree(left_tree_preorder, left_tree_inorder)
      head.right = self.buildTree(right_tree_preorder, right_tree_inorder)
      return head

if __name__ == "__main__":
  s = Solution()
