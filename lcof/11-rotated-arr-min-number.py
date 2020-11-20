# @Author: Hanyang
# @Date: 2020-11-20
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
      lens = len(numbers)
      for i in range(lens):
        if i+1 < lens and numbers[i] > numbers[i+1]:
          return numbers[i+1]
      return numbers[0]

if __name__ == "__main__":
  s = Solution()
