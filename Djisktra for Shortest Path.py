import csv
data=[]
with open(r'C:\Users\HU-Student\Desktop\connections.csv') as file:
    reader = csv.reader(file)
    for row in reader:
      if row!='':
        data.append(row)
cities = []
for v in data[0]:
  if v!='':
    cities.append(v)
Graph = {v:[] for v in data[0] if v!=''}

del data[0]
for i in data:
  if i[0] in cities:
    for j in range (len(i)-1):
      Graph[i[0]].append((cities[j], i[j+1]))

def enqueue(lst, node, weight):
    aa = []
    index=math.inf
    if len(lst)!=0:
      for i in range(len(lst)):
        if lst[i][0]==node:
          aa.append(lst[i])
          index=i
        else:
          lst.append((node, weight))
      if aa!=[]:
        if weight< aa[0][1]:
          lst[index] = (node, weight)
    else:  
      lst.append((node, weight))
def dequeue(PQ):
    a = PQ.pop(0)
    return(a)
    
def out_edges(G,u):
    return(G[u])
    
def addNodes(G,s):
    nodes = {}
    for key in G:
        nodes[key] = s
    return(nodes)
    
def getOutNeighbors(g,u):
    return(g[u])
import math
def getShortestPath (graph, fro , to):
	if  fro not in graph: return f"{fro} is not present in given Graph" 
	if  to not in graph: return f"{to} is not present in given Graph"
	PQ = []
	enqueue(PQ, fro, 0)
	Path = addNodes(graph, None)
	Dist = addNodes(graph , math.inf ) # A Dictionary of nodes, each set to infinity
	Dist[fro] = 0 		   # source node distance set to 0 by default
	while len(PQ) > 0:
		u = dequeue(PQ)
		children = getOutNeighbors(graph, u[0])
		for child,weight in children:
			alt = int(Dist[u[0]]) + int(weight)
			if alt < Dist[child]:
				Dist[child] = alt
				Path[child] = u[0]
				enqueue(PQ, child, alt)
	trajectory_teller=to
	dispos = to
	dipo = ''
	while trajectory_teller[-1]!= fro: #dispos != fro:
		trajectory_teller+= f" ot {Path[dispos]}" 
		dispos = Path[dispos]


	return trajectory_teller[::-1]
print(getShortestPath (Graph, 'Islamabad', 'Kaghan'))
