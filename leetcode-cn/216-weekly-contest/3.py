# @Author: Hanyang
# @Date: 2020-11-22
from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
      lens = len(nums)
      odd = [0]
      even = [nums[0]]
      for i in range(1, lens):
        if i % 2 == 0:
          even.append(even[i-1] + nums[i])
          odd.append(odd[i-1])
        else:
          odd.append(odd[i-1] + nums[i])
          even.append(even[i-1])
      res = 0
      for i in range(lens):
        # 左边
        left_odd = odd[i-1] if i-1>=0 else 0
        left_even = even[i-1] if i-1>=0 else 0

        # 右边
        right_odd = odd[lens-1] - odd[i]
        right_even = even[lens-1] - even[i]
        if left_odd + right_even == left_even + right_odd: res += 1
      return res

if __name__ == "__main__":
  s = Solution()
