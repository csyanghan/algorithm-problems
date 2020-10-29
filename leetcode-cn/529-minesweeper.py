# @Author: Hanyang
# @Date: 2020-10-29
from typing import List

class Solution:
  def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    self.board = board
    self.dir_x: List[int] = [0, 1, 0, -1, 1, 1, -1, -1]
    self.dir_y: List[int] = [1, 0, -1, 0, 1, -1, 1, -1]
    x: int = click[0]
    y: int = click[1]
    self.m: int = len(board)
    self.n: int = len(board[0])
    if self.board[x][y] == 'M':
      self.board[x][y] = 'X'
    else:
      self.dfs(x,y)
    return board

  def dfs(self, x, y):
    cnt = 0
    for i in range(8):
      nx = x + self.dir_x[i]
      ny = y + self.dir_y[i]
      if (nx < 0 or nx >= self.m or ny <0 or ny >= self.n):
        continue
      cnt += self.board[nx][ny] == 'M'
    if cnt > 0:
      self.board[x][y] = str(cnt)
    else:
      self.board[x][y] = 'B'
      for i in range(8):
        nx = x + self.dir_x[i]
        ny = y + self.dir_y[i]
        if (nx < 0 or nx >= self.m or ny <0 or ny >= self.n or self.board[nx][ny] != 'E'):
          continue
        self.dfs(nx, ny)

if __name__ == "__main__":
  s = Solution()
  board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
  click = [3,0]
  s.updateBoard(board, click)
  print(board)
