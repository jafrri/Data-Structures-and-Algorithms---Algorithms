import math
def enqueue(lst,s):
    lst.append(s)
    
def dequeue(lst):
    a = lst[0]
    del(lst[0])
    return(a)
    
def pop(lst):
    a = lst[0]
    del(lst[0])
    return(a)
    
def is_empty(lst):
    if len(lst) == 0:
        return(True)
    else:
        return(False)


def bfs(G,s):
    visited = {}
    level = {}
    parent = {}
    bfs_traversal = []
    queue = []
    
    for node in G:
        visited[node] = False
        parent[node] = None

        level[node] = math.inf
    
    visited[s] = True
    level[s] = 0
    enqueue(queue,s)
    
    while not is_empty(queue) == True:
        u = pop(queue)
        bfs_traversal.append(u)
        
        for v in G[u]:
            if not visited[v] == True:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                enqueue(queue,v)
    print(bfs_traversal)  # Visited nodes
    print(level) # Level of nodes
    print(parent) #Parent of nodes

print(bfs({1:[2,3],2:[3],3:[]},1))
