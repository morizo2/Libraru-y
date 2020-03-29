class LCA:
      
  def __init__(self,n,G,root):
    self.depth = [0] * n
    self.parent = [[0] * n for i in range((n-1).bit_length())]
    self.n = n
    self.G = G
    self.root = root
    self.logn = (n-1).bit_length()
    self.setdepth(root,-1,0)
    self.set_doubling_parent()
  
  def setdepth(self,node,pre,d):
    self.depth[node] = d
    self.parent[0][node] = pre
    for vi in self.G[node]:
      if vi == pre: continue
      self.setdepth(vi,node,d + 1)
  
  def set_doubling_parent(self):
    for k in range(self.logn-1):
      for v in range(n):
        if self.parent[k][v] < 0: self.parent[k+1][v] = -1
        else: self.parent[k+1][v] = self.parent[k][self.parent[k][v]]
  
  def lca(self,u,v):
    # 高度調整
    if self.depth[u] > self.depth[v]: u,v = v,u
    for k in range(self.logn):
      if (self.depth[v] - self.depth[u]) >> k & 1:
        v = self.parent[k][v]
    # 2部探索
    if u == v:
      return u
    for k in range(self.logn-1,-1,-1):
      if self.parent[k][u] != self.parent[k][v]:
        u = self.parent[k][u]
        v = self.parent[k][v]
    return self.parent[0][u]