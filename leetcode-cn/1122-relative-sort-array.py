# @Author: Hanyang
# @Date: 2020-11-14
from typing import List

# 自定义排序
class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    len_arr2 = len(arr2)
    hashmap = {}
    for i in range(len_arr2):
      hashmap[arr2[i]] = i
    def key_func(x):
      if hashmap.get(x) != None:
        return hashmap[x]
      return x + len_arr2
    return sorted(arr1, key=key_func)
    
# 计算排序
class Solution_1:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    frequency = [0] * 1001
    len1 = len(arr1)
    len2 = len(arr2)
    for i in range(len1):
      frequency[arr1[i]] += 1
    res = []
    for i in range(len2):
      res.extend([arr2[i]] * frequency[arr2[i]])
      frequency[arr2[i]] = 0
    for i in range(1001):
      if frequency[i] != 0:
        res.extend([i]* frequency[i])
    return res

if __name__ == "__main__":
  s = Solution()
