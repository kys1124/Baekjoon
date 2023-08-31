N, M = map(int,input().split())

trees = list(map(int, input().split()))
trees.sort()

def cal_tree(trees, h):
    sm = 0
    for x in trees:
        sm += max(x-h,0)
    return sm

ans = 0
left = 0
right =trees[-1]

while left<=right:
    mid = (left+right)//2

    tree = cal_tree(trees,mid)
    if tree>M:
        ans = mid
        left =mid+1

    elif tree==M:
        ans = mid
        break
    else:
        right = mid-1

print(ans)