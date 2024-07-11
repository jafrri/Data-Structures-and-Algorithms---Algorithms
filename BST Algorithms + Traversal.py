def insert(bst,key):
  if bst == {}:
    bst['value'] = key
    bst['left'] = {}
    bst['right'] = {}
  else:
    if key < bst['value']:
      insert(bst['left'],key)
    elif key > bst['value']:
      insert(bst['right'],key)

bst = {}
lst = [8,3,10,1,6,14,4,7,13]
for i in lst:
  insert(bst,i)
print(bst)

    
def exist(bst,key):
  if bst == {}:
      return(False)
  elif bst['value'] == key:
    return(True)
  else:
    if key > bst["value"]:
      return exist(bst['right'],key)
    elif key < bst['value']:
      return exist(bst['left'],key)



print(exist(bst,3))

def get_node(bst,key):   # Helper Function to be used in minimum and maximum
    if bst == {}:
      return(False)
    elif bst['value'] == key:
      return(bst)
    else:
      if key > bst["value"]:
        return get_node(bst['right'],key)
      elif key < bst['value']:
        return get_node(bst['left'],key)

def minimum(bst,startingnode):
  u = get_node(bst,startingnode)
  while u['left'] != {}:
    u = u['left']
  return(u['value'])

print(minimum(bst,6))

def maximum(bst,startingnode):
  u = get_node(bst,startingnode)
  while u['right'] != {}:
    u = u['right']
  return(u['value'])

print(maximum(bst,6))
  





def inorder_traversal(bst):
    if bst == {}:
      return([])
    else:
      return(inorder_traversal(bst['left'])+[bst['value']]+inorder_traversal(bst['right']))

print(inorder_traversal(bst))

  

def preorder_traversal(bst):
  if bst == {}:
    return([])
  else:
    return([bst['value']]+preorder_traversal(bst['left']) + preorder_traversal(bst['right']))

print(preorder_traversal(bst))

def postorder_traversal(bst):
  if bst == {}:
    return([])
  else:
    return(postorder_traversal(bst['left'])+postorder_traversal(bst['right'])+[bst['value']])

print(postorder_traversal(bst))
