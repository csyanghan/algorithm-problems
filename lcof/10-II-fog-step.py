# @Author: Hanyang
# @Date: 2020-11-18

class Solution:
    def numWays(self, n: int) -> int:
      if n == 0: return 1
      if n == 1: return 1
      n = n -1
      f0, f1 = 1, 1
      while n > 0:
        f0, f1 = f1, f0+f1
        f0 = int(f0 %(1e9 +7))
        f1 = int(f1 %(1e9 +7))
        n -= 1
      return f1

if __name__ == "__main__":
  s = Solution()
