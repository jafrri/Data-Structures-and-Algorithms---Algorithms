def enqueue(Q,label,p):
    for i in range(len(Q)):
        if Q[i][0] == label:
            del(Q[i])
            break
    for j in range(len(Q)):
        if Q[j][1] > p:
            Q.insert(i,(label,p))
            return
    Q.append((label,p))
    return

def dequeue(PQ):
    a = PQ.pop(0)
    return(a)
    
def out_edges(G,u):
    return(G[u])
    
def addnodes(G,s):
    nodes = {}
    for key in G:
        nodes[key] = s
    return(nodes)

def getShortestPath2(G,fro,to):
    Dist = addnodes(G,math.inf)     # Shortest Distance Dictionary to all nodes from a specific node
    Dist[fro] = 0
    PQ = []
    parent = {}     # Parents dictionary of all nodes
    for node in G:
      parent[node] = None

    enqueue(PQ,fro,0)
    
    while len(PQ)> 0:
        u = dequeue(PQ)
        children = out_edges(G,u[0])
        
        for child,weight in children:
            alt = int(Dist[u[0]]) + weight
            if (alt) < (Dist[child]):
                enqueue(PQ,child,alt)
                Dist[child] = alt
                parent[child] = u[0]
                
    
    lst = []
    lst.append(to)
    lstt = []
    distance = Dist[to]   # Returns Shortest Distance
    while lst[-1] != fro:
      value = lst[-1]
      child = parent[value]
      lst.append(child)
    ls = lst[::-1]
    for i in range(len(lst)-1):
      tup1 = (ls[i],ls[i+1])
      lstt.append(tup1)
    return(lstt)  # Returns Shortest Path
