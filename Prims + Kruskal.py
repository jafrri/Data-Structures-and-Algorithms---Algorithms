# Prims
# Uses Priority Enqueue

def MSTPrims(G,SV):
    r = random_node(G)  # random node from Graph
    PQ = []
    enqueue(PQ,SV,0)
    Cost = addNodes_mod(G,math.inf)
    MST = addNodes_mod(G,None)
    Included = addNodes_mod(G,False)
    
    
    while len(PQ) > 0:
        u = dequeue(PQ)
        Included[u] = True
        
        children = G[u[0]]
        
        for child,weight in children:
            
            if not Included[child] and weight < Cost[child]:
                Cost[child] = weight
                MST[child] = (u[0],weight)
                enqueue(PQ,child,weight)
                
    lst = []
    for i in MST:
      if MST[i] is not None:
        value = MST[i]
        tup = (value[0],i,value[-1])
        lst.append(tup)
    return(lst)


# Kruskals
# Uses Disjoint Set

def union_find(G):
    UF = {}
    c = 0
    for node in G:
        UF[node] = c
        c += 1
    return(UF)



def find(UF,u):
    return(UF[u])


def union(UF,u,v):
    new_parent = UF[v]
    old_parent = UF[u]
    for node in UF:
        if UF[node] == old_parent:
            UF[node] = new_parent
def MSTKruskals(EL):
    PQ = []
    for u in G:
        for v, weight in G[u]:
            enqueue(PQ,(u,v),weight)
    MST = []
    UF = union_find(EL)
    
    while len(PQ) > 0:
      u,v = dequeue(PQ)
      if  find(UF,u[0]) != find(UF,u[1]):
        MST.append((u[0],u[1],v))
        union(UF,u[0],u[1])
    return(MST)
