# @Author: Hanyang
# @Date: 2020-11-18
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
      if head == None: return []
      stack = [head.val]
      while head.next:
        head = head.next
        stack.append(head.val)
      res = []
      while len(stack):
        res.append(stack.pop())
      return res

if __name__ == "__main__":
  s = Solution()
