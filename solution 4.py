def singleNumber(nums):
    return 2*sum(set(nums))-sum(nums)
    a=list(map(int,input().split(',')))
    print(int(singleNumber(a)))