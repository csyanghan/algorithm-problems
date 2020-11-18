# @Author: Hanyang
# @Date: 2020-11-18

class CQueue:

    def __init__(self):
      self.stack1 = []
      self.stack2 = []

    def appendTail(self, value: int) -> None:
      while len(self.stack2):
        self.stack1.append(self.stack2.pop())
      self.stack1.append(value)


    def deleteHead(self) -> int:
      while len(self.stack1):
        self.stack2.append(self.stack1.pop())
      if len(self.stack2):
        return self.stack2.pop()
      return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

if __name__ == "__main__":
  # s = Solution()
  pass
