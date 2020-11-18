# @Author: Hanyang
# @Date: 2020-11-18
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      lens = len(gas)
      for i in range(lens):
        if cost[i] > gas[i]:
          continue
        remain_gas = gas[i] - cost[i]
        j = (i + 1) % lens
        while remain_gas + gas[j] >= cost[j]:
          remain_gas = remain_gas + gas[j] - cost[j]
          j = (j+1) % lens
          if j == i:
            return i
      return -1


if __name__ == "__main__":
  s = Solution()
  print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
