# @Author: Hanyang
# @Date: 2020-11-22

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
      res = []
      start = 26
      while n !=0:
        if n-1 <= k - start:
          res.append(start)
          n -= 1
          k -= start
        else:
          start -= 1
      res = sorted(res)
      return ''.join(list(map(lambda x: chr(x+96), res)))

s = Solution()
print(s.getSmallestString(5, 73))
