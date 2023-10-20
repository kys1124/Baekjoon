N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))


card = [i for i in range(N)]
origin = card[:]
duplicate = set()
player = dict()
def shuffle(card, S):
    new = [0]*N
    for i in range(N):
        new[S[i]] = card[i]
    return new

def give(card, player):
    for i in range(N):
        player[i%3].append(card[i])
    return player

def check(card, player, P):
    for i in range(N):
        if card[i] in set(player[P[i]]):
            continue
        else:
            return False
    return True


ans = 0
while True:
    player[0] = []
    player[1] = []
    player[2] = []
    player = give(card, player)
    if check(origin, player, P):
        break

    if tuple(player[0] + player[1] + player[2]) in duplicate:
        ans = -1
        break

    duplicate.add(tuple(player[0]+player[1]+player[2]))
    card = shuffle(card,S)
    ans +=1

print(ans)