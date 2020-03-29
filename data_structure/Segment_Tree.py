class SegmentTree:
  __slots__ = ['ide','n','seg','segfunc']

  def __init__(self,size,func,element):
    self.segfunc = func
    self.ide = element
    # self.size = sizeを超える最小の2冪の数
    self.n = 2 ** (size-1).bit_length()
    # 全てのnodeの数は(2*n-1)個
    # 上にn-1個,最下段にn個
    self.seg = [self.ide] * (2*self.n-1)

  def apply(self,array):
    arraysize = len(array)
    # 配列埋め込み
    for i in range(arraysize):
      self.seg[self.n-1+i] = array[i]
    # 上にあげる
    for i in range(self.n-2,-1,-1):
      self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

  def update(self,k,x):
    k += self.n -1
    self.seg[k] = x
    while k:
      k = (k-1)//2
      self.seg[k] = self.segfunc(self.seg[2*k+1],self.seg[2*k+2])

  def query(self,l,r):
    # 半開区間[l,r)
    l += self.n-1; r += self.n-1
    res = self.ide
    while l < r:
      if l & 1 == 0:
        res = self.segfunc(res,self.seg[l])
        l += 1
      if r & 1 == 0:
        res = self.segfunc(res,self.seg[r-1])
      l = (l-1)//2; r = (r-1)//2
    return res