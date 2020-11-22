# @Author: Hanyang
# @Date: 2020-11-22
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
      s1 = ''.join(word1)
      s2 = ''.join(word2)
      return s1 == s2

if __name__ == "__main__":
  s = Solution()
