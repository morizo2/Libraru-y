import heapq
inf = float("inf")

def dijktra(g,s):
  n=len(g)
  dist = [inf]*n
  dist[s] = 0
  hq=[]
  heapq.heappush(hq,(dist[s],s))
  while hq:
    cost,u =heapq.heappop(hq)
    if dist[u] < cost:
      continue
    for v,c in g[u]:
      if dist[v] <= dist[u] +c:
        continue
      dist[v] = dist[u] + c
      heapq.heappush(hq,(dist[v],v))
  return dist