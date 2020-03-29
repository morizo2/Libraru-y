import collections

def Topological_Sort(G):
  # DAGの隣接リストを受け取って、トポロジカルソートしたリストを返す
  V=len(G)
  div=[0]*V
  for gi in G:
    for ei  in gi:
      div[ei]+=1
  used=[0]*V
  result=[]

  def bfs(node):
    que = collections.deque([node])
    used[node] = 1
    while que:
      tmp = que.popleft()
      result.append(tmp)
      for v in G[tmp]:
        div[v] -= 1
        if div[v] == 0 and not used[v]:
          que.append(v)
          used[v] = 1

  for i in range(V):
      if div[i]==0 and not used[i]:
          bfs(i)
  return result