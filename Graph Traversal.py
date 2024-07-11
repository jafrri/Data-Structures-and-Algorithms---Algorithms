def addnodes_g(G):
  nodes = {}
  for key in G:
    nodes[key] = False
  return(nodes)

def push(S,s):
  S.append(s)

def pop(S):
  a = S.pop()
  return(a)

def out_edges(G,u):
  return(G[u])
G = {0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}

def dfs_tree(G,s):
    S = []
    push(S,s)
    visited = addnodes_g(G)
    visited[s] = True
    while len(S) > 0:
        u = pop(S)
        if visited[u] == True:
          visited[u] == False
          print(u)
          childr = (out_edges(G,u))
          children = childr[::-1]

          for child in children:
            push(S,child)

dfs_tree(G,0)
