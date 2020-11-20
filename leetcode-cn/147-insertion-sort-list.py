# @Author: Hanyang
# @Date: 2020-11-20
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
      if head is None: return None
      dummyHead = ListNode(0)
      dummyHead.next = head
      sorted_end = head
      cur = head.next
      while cur:
        if sorted_end.val <= cur.val:
          sorted_end = sorted_end.next
        else:
          pre = dummyHead
          while pre.next.val <= cur.val:
            pre = pre.next
          sorted_end.next = cur.next
          cur.next = pre.next
          pre.next = cur
        cur = sorted_end.next
      return dummyHead.next
          


if __name__ == "__main__":
  s = Solution()
