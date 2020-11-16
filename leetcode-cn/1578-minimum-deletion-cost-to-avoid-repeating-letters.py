# @Author: Hanyang
# @Date: 2020-11-16
from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
      lens = len(s)
      res = 0
      for i in range(lens-1):
        if (s[i] == s[i+1]):
          res += min(cost[i], cost[i+1])
          # 太强了
          if cost[i] > cost[i+1]: cost[i], cost[i+1] = cost[i+1], cost[i]
      return res

class Solution_1:
    def minCost(self, s: str, cost: List[int]) -> int:
        # 官方解答, 先加上当前值, 最后再减去最大值(没有相同则减去当前值)
        lens = len(s)
        maxValue = 0
        i = 0
        res = 0
        while i<lens:
          cur = s[i]
          maxValue = 0
          inner_sum = 0
          while(i<lens and s[i] == cur):
            maxValue = max(maxValue, cost[i])
            inner_sum += cost[i]
            i += 1
          res += inner_sum - maxValue
        return res

if __name__ == "__main__":
  s = Solution()
