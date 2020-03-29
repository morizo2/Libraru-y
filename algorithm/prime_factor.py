def prime_factor(n):
  ass = []
  for i in range(2,int(n**0.5)+1):
    count=0
    while n % i==0:
      count+=1
      n = n//i
    if count!=0:
      ass.append((i,count))
  if n != 1:
    ass.append((n,1))
  return ass