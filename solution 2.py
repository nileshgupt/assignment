def printintersection(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)
    return (list(set2 & set1))
    a=list(map(int,input().split(',')))
    b=list(map(int,input().split(',')))
    print(printintersection(a,b))