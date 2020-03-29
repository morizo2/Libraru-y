class BIT:
  # [1,size]に値が入ってる1-indexであることに注意
  def __init__(self,size):
    self.data = [0]*(size+1)
    self.size = size
  
  # [1,n]までの総和
  def sum(self,n):
    res = 0
    while n > 0:
      res += self.data[n]
      n -= n & -n
    return res
  
  # k番目の値をxに更新
  def update(self,k,x):
    while k < self.size + 1:
      self.data[k] += x
      k += k & -k
