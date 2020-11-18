# @Author: Hanyang
# @Date: 2020-11-17
from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
      cells = {}
      for i in range(R):
        for j in range(C):
          distance = abs(i-r0) + abs(j-c0)
          if cells.get(distance) == None:
            cells[distance] = [[i, j]]
          else:
            cells[distance].append((i, j))
      sorted_key = sorted(cells.keys())
      res = []
      for key in sorted_key:
        res.extend(cells[key])
      return res


if __name__ == "__main__":
  s = Solution()
