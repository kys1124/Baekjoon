N= int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

lst1.sort()

def binary_search(num,lst):
    left = 0
    right = len(lst)-1
    
    while left<=right:
        mid = (left+right)//2
        if lst[mid]==num:
            return True

        elif lst[mid]>num:
            right = mid-1
        else:
            left=mid+1

    return False

for x in lst2:
    if binary_search(x, lst1):
        print(1)
    else:
        print(0)