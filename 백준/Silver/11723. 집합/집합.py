import sys
input = sys.stdin.readline
M = int(input())

s = set()
for _ in range(M):
    command = input().split()
    if len(command)==1:
        if command[0] == 'all':
            s = set([x for x in range(1, 21)])

        else:
            s = set()

    else:
        command, x = command[0], command[1]
        x = int(x)
    if command == 'add':
        s.add(x)

    elif command == 'remove':
        s.discard(x)

    elif command == 'check':
        if x in s:
            print(1)
        else:
            print(0)

    elif command == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)



