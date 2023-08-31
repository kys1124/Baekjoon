h = []
for _ in range(9):
    h.append(int(input()))

h.sort()
answer =[]
def find(lst, value, answer):
    real = sum(lst[1:-1])
    if value==real:
        answer+=lst[1:-1]
        return answer
    elif real<value:
        answer.append(lst[-1])
        return find(lst[:-1],value-lst[-1], answer)
    else:
        answer.append(lst[0])
        return find(lst[1:], value-lst[0], answer)

for x in sorted(find(h,100,answer)):
    print(x)