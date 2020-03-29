class SWAG:
  def __init__(self,func,ide):
    self.ide = ide
    self.func = func
    self.front = []
    self.back = []
  
  def push(self,x):
    # 累積の結果を残す
    if self.back: y = self.func(self.back[-1][1],x)
    else: y = x
    self.back.append((x,y))
  
  def pop(self):
    if not self.front:
      while self.back:
        x,y = self.back.pop()
        if self.front: y = self.func(self.front[-1][1],x)
        else: y = x
        self.front.append((x,y))
    return self.front.pop()[1]
  
  def fold_all(self):
    y = self.ide
    if self.front: y = self.func(self.front[-1][1],y)
    if self.back: y = self.func(self.back[-1][1],y)
    return y