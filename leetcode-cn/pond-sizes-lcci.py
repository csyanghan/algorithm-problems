class Solution:
  def pondSizes(self, land):
    self.ans = []
    self.land = land
    self.n = len(land)
    self.m = len(land[0])
    for i in range(self.n):
      for j in range(self.m):
        if (self.land[i][j] == 0):
          self.ans.append(1+self.dfs(i, j))
    return sorted(self.ans)
  
  def dfs(self, x,y):
    self.land[x][y] = 1
    xdir = [-1,0, 1]
    ydir = [-1,0,1]
    ans = 0
    for dx in xdir:
      for dy in ydir:
        nx = x + dx
        ny = y + dy
        if (nx >=0 and nx < self.n and ny >=0 and ny < self.m and (self.land[nx][ny] == 0)):
          ans = ans + 1 + self.dfs(nx, ny)
    return ans

if __name__ == '__main__':
  pand = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]
  ]
  s = Solution()
  print(s.pondSizes(pand))