

def Kruskals(G):
    PQ = []
    for u in G:
        for v, weight in G[u]:
            enqueue(PQ,(u,v),weight)


    MST = []
     while len(PQ) > 0:
         u,v = dequeue(PQ)
         if not find(u) != find(v):
             MST.append((u,v))
             union(u,v)
    return(MST)


def union_find(G):
    UF = []
    c = 0
    for node in G:
        UF[node] = c
        c += 1
    return(UF)



def find(UF,u):
    return(UF[u])


def union(UF,u,v):
    new_parent = UF[u]
    old_parent = UF[v]
    for node in UF:
        if UF[node] = old_parent:
            UF[node] = new_parent

def random_nodes(G):
    nodes = list(G.keys())
    x = randint(0,len(nodes)-1)
    for i in range(len(nodes)):
        if i == x:
            return(nodes[i])


        
    
