# @Author: Hanyang
# @Date: 2020-11-17
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
      hashmap = {}
      lens = len(nums)
      for i in range(lens):
        if hashmap.get(nums[i]) == None:
          hashmap[nums[i]] = 1
        else:
          return nums[i]

if __name__ == "__main__":
  s = Solution()
