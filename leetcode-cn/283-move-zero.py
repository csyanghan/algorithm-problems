# @Author: Hanyang
# @Date: 2020-11-19
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      lens = len(nums)
      for i in range(lens):
        if nums[i] == 0:
          j = i+1
          if j < lens:
            while j <lens and nums[j] == 0:
              j += 1
            if j <lens and nums[j] != 0:
              nums[i], nums[j] = nums[j], nums[i]
      return nums

if __name__ == "__main__":
  s = Solution()
  print(s.moveZeroes([0,1,0,3,12]))
