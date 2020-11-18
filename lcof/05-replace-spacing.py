# @Author: Hanyang
# @Date: 2020-11-17

class Solution:
    def replaceSpace(self, s: str) -> str:
      res = ''
      lens = len(s)
      for i in range(lens):
        if s[i] == ' ':
          res += '%20'
        else:
          res += s[i]
      return res

if __name__ == "__main__":
  s = Solution()
