# @Author: Hanyang
# @Date: 2020-11-15
# https://leetcode-cn.com/contest/weekly-contest-215/
from typing import List

class Solution:
    # 只取左半部分的和，只取右半部分的和，取左右两部分的和
    def minOperations(self, nums: List[int], x: int) -> int:
      if sum(nums) < x: return -1
      lens = len(nums)
      prefix = 0
      pre_hashmap = {}
      for i in range(lens):
        prefix += nums[i]
        if prefix > x: break
        pre_hashmap[prefix] = i+1
      sub = 0
      sub_hashmap = {}
      for i in range(lens-1, -1, -1):
        sub += nums[i]
        if sub > x: break
        sub_hashmap[sub] = lens - i
      res = min(pre_hashmap.get(x, float('inf')), sub_hashmap.get(x, float('inf')))
      for pre_sum in pre_hashmap:
        if x - pre_sum in sub_hashmap:
          step = pre_hashmap[pre_sum] + sub_hashmap[x-pre_sum]
          if step <= lens:
            res = min(res, step)
      return res if res != float('inf') else -1

if __name__ == "__main__":
  s = Solution()
  print(float('inf'))