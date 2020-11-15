# @Author: Hanyang
# @Date: 2020-11-15

class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    lens = len(num)
    if lens == k: return '0'
    res = ''
    for i in range(lens):
      if k > 0:
        # !!!前面比后面大的全部丢掉!!!
        if i+1 < lens and num[i] > num[i+1]:
          k -= 1
        else:
          res += num[i]
      else:
        res += num[i]
    if k>0:
      res = res[:-k]
    while len(res) >= 1 and res[0] == '0':
      res = res[1:]
    return res if res else '0'

class Solution_1:
  def removeKdigits(self, num: str, k: int) -> str:
    lens = len(num)
    if lens == k: return '0'
    stack = []
    remian = lens - k
    for digit in num:
      while k and stack and stack[-1] > digit:
        stack.pop()
        k -= 1
      stack.append(digit)
    return ''.join(stack[:remian]).lstrip('0') or '0'

if __name__ == "__main__":
  s = Solution_1()
  print(s.removeKdigits('1234567890', 9))
