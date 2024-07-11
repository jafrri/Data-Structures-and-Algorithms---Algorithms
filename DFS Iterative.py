def push(lst,s):
    lst.append(s)
    
def pop(lst):
    a = lst[-1]
    del(lst[-1])
    return(a)
    
def is_empty(lst):
    if len(lst) == 0:
        return(True)
    else:
        return(False)


def dfs(G , u):
    visited = []
    stack = []
    push(stack,u)
    while is_empty(stack) == False:
        v = pop(stack)
        if v not in visited:
            visited.append(v)
            a = G[v]
            rev = a[::-1]
            stack.extend(rev)
    return(visited)



# Option 2

def dfs2(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # add all unexplored, adjacent nodes to stack
            stack.extend(set(graph[vertex]) - visited)

print(dfs({1:[3,2],3:[2],2:[]},1))
