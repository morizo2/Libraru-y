class InverseTable:
  __slots__ = ['mod', 'In', 'fac', 'Ifac']

  def __init__(self, mod, maxnum):
    self.mod = mod; self.In = [0, 1]
    self.fac = [1, 1]; self.Ifac = [1, 1]
    for i in range( 2, maxnum + 1 ):
      self.In.append( ( -self.In[mod % i] * (mod//i) ) % mod )
      self.fac.append( ( self.fac[-1] * i ) % mod )
      self.Ifac.append( (self.Ifac[-1] * self.In[-1]) % mod )
        
  def cmb(self, n, r):
    if ( r<0 or r>n ): return 0
    r = min(r, n-r)
    return self.fac[n] * self.Ifac[r] * self.Ifac[n-r] % self.mod
    
  def per(self, n, r):
    if ( r<0 or r>n ): return 0
    return self.fac[n] * self.Ifac[n-r] % self.mod
