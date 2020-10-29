n = 4
a = [1,2,4,7]
k = 13

# 已经从前i项得到了和sum，然后对于i项之后的进行分支
def dfs(i, sum):
  # 如果前n项都计算过了，则返回sum是否与k相等
  if i == n: return sum == k
  # 不加上a[i]的情况
  if dfs(i + 1, sum): return True
  # 加上a[i]的情况
  if dfs(i+1, sum + a[i]): return True
  # 无论是否加上a[i]都不能凑成k就返回false
  return False

def solve():
  if dfs(0,0): print('Yes')
  else: print('No')

if __name__ == '__main__':
  solve()
