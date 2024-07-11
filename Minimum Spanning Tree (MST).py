
def mst(G):
    r = random_node(G)  # random node from Graph
    PQ = []
    enqueue(PQ,r,0)
    
    Cost = addNodes(G,math.inf)
    MST = addNodes(G,None)
    Included = addNodes(G,False)
    
    
    while len(PQ) > 0:
        u = dequeue(PQ)
        Included[u] = True
        
        children = G[u]
        
        for child,weight in children:
            
            if not Included[child] and weight < Cost[child]:
                Cost[child] = weight
                MST[child] = u
                enqueue(PQ,child,weight)
                
    return(MST) 
                
            
