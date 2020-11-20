# @Author: Hanyang
# @Date: 2020-11-20
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
      max_n = int('9'*n)
      return list(range(1, max_n+1))

if __name__ == "__main__":
  s = Solution()
  print(s.printNumbers(1))
