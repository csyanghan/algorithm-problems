# @Author: Hanyang
# @Date: 2020-11-16
from typing import List

class Solution:
    # tip: 先放矮子(若身高相同则k越大越矮, k越大表示前面留的空位越多),因为他们对后面的人无影响
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
      people.sort(key=lambda x: (x[0], -x[1]))
      lens = len(people)
      res = [0] * lens
      for i in range(lens):
        idx = people[i][1] + 1
        for j in range(lens):
          if res[j] == 0:
            idx -= 1
            if idx == 0:
              res[j] = people[i]
              break
      return res


if __name__ == "__main__":
  s = Solution()
  print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
