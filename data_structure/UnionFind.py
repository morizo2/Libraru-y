class UnionFind:
  __slots__ = ['id','sz']

  def __init__(self, n):
    self.id = [-1] * n
    self.sz = n

  def root(self, x):
    if self.id[x] < 0:
      return x
    else:
      self.id[x] = self.root(self.id[x])
      return self.id[x]

  def find(self, x, y):
    return self.root(x) == self.root(y)

  def union(self, x, y):
    s1, s2 = self.root(x), self.root(y)
    if s1 != s2:
      if self.id[s1] <= self.id[s2]:
        self.id[s1] += self.id[s2]
        self.id[s2] = s1
      else:
        self.id[s2] += self.id[s1]
        self.id[s1] = s2
      self.sz-=1
      return True
    return False

