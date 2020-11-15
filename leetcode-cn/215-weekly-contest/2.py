# @Author: Hanyang
# @Date: 2020-11-15
# https://leetcode-cn.com/contest/weekly-contest-215/

class Solution:
    # 字符出现次数组成的列表仅可能出现的顺序不同，排序后对比即可。（因为无论是更换字符位置，还是变换字符，都是只会仅仅改变这个列表顺序）。
    def closeStrings(self, word1: str, word2: str) -> bool:
      len_1 = len(word1)
      len_2 = len(word2)
      if len_1 != len_2: return False
      hashmap1 = {}
      hashmap2 = {}
      for i in range(len_1):
        before_1 = hashmap1.get(word1[i], 0)
        hashmap1[word1[i]] = before_1 + 1
        before_2 = hashmap2.get(word2[i], 0)
        hashmap2[word2[i]] = before_2 + 1
      return sorted(hashmap1.values()) == sorted(hashmap2.values()) and set(word1) == set(word2)

if __name__ == "__main__":
  s = Solution()
  print(s.closeStrings('cabbba', 'abbccc'))
