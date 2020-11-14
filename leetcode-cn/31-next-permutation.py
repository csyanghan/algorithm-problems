# @Author: Hanyang
# @Date: 2020-11-14
from typing import List

#  思路就是从右往左，找到第一个左边的数小于右边的数
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens <= 1:
          return nums
        idx = lens - 1
        while idx >=1 and nums[idx-1] >= nums[idx]:
          idx -= 1
        idx -= 1 # 找出从 idx 开始的最大的数和 idx 交换
        # 冒泡排序
        for i in range(lens-1, idx, -1):
          for j in range(i-1, idx, -1):
            if nums[j] > nums[i]:
              nums[i], nums[j] = nums[j], nums[i]
        if idx != -1:
          for i in range(idx+1, lens, 1):
            if nums[i] > nums[idx]:
              nums[idx], nums[i] = nums[i], nums[idx]
              break


if __name__ == "__main__":
  s = Solution()
