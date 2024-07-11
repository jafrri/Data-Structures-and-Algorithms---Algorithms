# Bubble Sort    O(n^2)

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return(lst)


# Insertion Sort   O(n^2)

def Insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i -1
        while j >= 0 and lst[i] < lst[j]:
            j = j - 1
        lst.insert(j+1,lst[i])
        del(lst[i+1])
    return(lst)

# Selection Sort   O(n^2)

def Selection_sort(lst):
    for i in range(len(lst)):
        mini = i
        for j in range(mini,len(lst),1):
            if lst[j] < lst[mini]:
                mini = j
        lst[i],lst[mini] = lst[mini],lst[i]
    return(lst)

# Merge Sort    O(n*logn)

def Merge_sort(lst):
    if len(lst) == 1:
        return(lst)
    else:
        mid = len(lst) // 2
        left,right = Merge_sort(lst[0:mid]) , Merge_sort(lst[mid::])
        return(merge(left,right))


def merge(left, right):
    i,j = 0,0
    lst  = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i = i + 1
        else:
            lst.append(right[j])
            j = j + 1
    lst = lst + left[i:]
    lst = lst + right[j:]
    return(lst)

# Quick Sort   O(n^2)

def Quick_sort(lst):
    if len(lst) <= 1:
        return(lst)
    else:
        pivot = lst[0]
        lesser, greater = partition(lst,pivot)
        less = Quick_sort(lesser)
        great = Quick_sort(greater)
        return(less+[pivot]+great)

def partition(lst, pivot):
    del(lst[0])
    less,great = [],[]
    for i in lst:
        if i <= pivot:
            less.append(i)
        elif i > pivot:
            great.append(i)
    return(less,great)

    











    

                
