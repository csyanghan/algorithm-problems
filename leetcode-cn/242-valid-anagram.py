# @Author: Hanyang
# @Date: 2020-11-22

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      hashmap1 = {}
      hashmap2 = {}
      len1 = len(s)
      len2 = len(t)
      if len1 != len2: return False
      for i in range(len1):
        key1 = ord(s[i])
        key2 = ord(t[i])
        v1 = hashmap1.get(key1)
        v2 = hashmap2.get(key2)
        if v1: hashmap1[key1] = v1 + 1
        else: hashmap1[key1] = 1
        if v2: hashmap2[key2] = v2 + 1
        else: hashmap2[key2] = 1
      for key in hashmap1:
        if hashmap2.get(key) is None: return False
        if hashmap1[key] != hashmap2[key]: return False
      return True

if __name__ == "__main__":
  s = Solution()
