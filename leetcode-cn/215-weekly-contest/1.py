# @Author: Hanyang
# @Date: 2020-11-15
# https://leetcode-cn.com/contest/weekly-contest-215/

from typing import List

class OrderedStream:

    def __init__(self, n: int):
      self.ptr = 1
      self.n = n
      self.stream = [0] * 1001

    def insert(self, id: int, value: str) -> List[str]:
      self.stream[id] = value
      res = []
      if self.stream[self.ptr] != 0:
        res.append(self.stream[self.ptr])
        while self.stream[self.ptr+1] !=0:
          self.ptr += 1
          res.append(self.stream[self.ptr])
        self.ptr += 1
      return res

if __name__ == "__main__":
  os = OrderedStream(5)
  print(os.insert(3, "ccccc")) # 插入 (3, "ccccc")，返回 []
  print(os.insert(1, "aaaaa")) # 插入 (1, "aaaaa")，返回 ["aaaaa"]
  print(os.insert(2, "bbbbb")) # 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
  print(os.insert(5, "eeeee")) # 插入 (5, "eeeee")，返回 []
  print(os.insert(4, "ddddd")) # 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
