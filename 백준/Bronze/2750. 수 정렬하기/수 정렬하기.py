N = int(input())
lst = [int(input()) for _ in range(N)]
def quick_sort(arr):
    if len(arr)<2:
        return arr
    pivot=arr[len(arr)//2]
    left,equal,right = [],[],[]

    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            right.append(x)
    return quick_sort(left)+equal+quick_sort(right)

#
#
# for x in merge_sort(lst):
#     print(x)

for x in quick_sort(lst):
    print(x)