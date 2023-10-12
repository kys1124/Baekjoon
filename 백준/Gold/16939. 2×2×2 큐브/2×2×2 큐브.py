lst = list(map(int, input().split()))

cube1 = [0,2,1,3,4,6,5,7,8,10,9,11,21,23,20,22]
cube2 = [12,13,14,15,4,5,6,7,16,17,18,19,20,21,22,23]
cube3 = [0,1,2,3,12,14,13,15,10,11,8,9,17,19,16,18]
check_dic = {0:8,8:0, 12:16,16:12,4:20,20:4}

def check(cube1, cube2, lst):
    idx_lst = []
    for i in range(0,24,4):
        cur_num = lst[i]
        if lst[i+1]==cur_num and lst[i+2]==cur_num and lst[i+3]==cur_num:
            idx_lst.append(i)
    if len(idx_lst)!=2:
        return False
    a,b = idx_lst[0], idx_lst[1]
    if check_dic[a]!=b:
        return False

    if a not in cube2:
        for idx in range(0,len(cube2),4):
            if len(set([lst[cube2[idx]],lst[cube2[idx+1]], lst[cube2[(idx+6)%16]], lst[cube2[(idx+7)%16]]]))==1:
                continue
            else:
                break
        else:
            return True

        for idx in range(0, len(cube2), 4):
            if len(set([lst[cube2[idx]], lst[cube2[idx + 1]], lst[cube2[(idx-1) % 16]],
                        lst[cube2[(idx-2) % 16]]])) == 1:
                continue
            else:
                break
        else:
            return True

        return False
    elif a not in cube1:
        for idx in range(0, len(cube2), 4):
            if len(set([lst[cube1[idx]], lst[cube1[idx + 1]], lst[cube1[(idx + 6) % 16]],
                        lst[cube1[(idx + 7) % 16]]])) == 1:
                continue
            else:
                break
        else:
            return True

        for idx in range(0, len(cube2), 4):
            if len(set([lst[cube1[idx]], lst[cube1[idx + 1]], lst[cube1[(idx - 1) % 16]],
                        lst[cube1[(idx - 2) % 16]]])) == 1:
                continue
            else:
                break
        else:
            return True

        return False
    else:
        for idx in range(0, len(cube3), 4):
            if len(set([lst[cube3[idx]], lst[cube3[idx + 1]], lst[cube3[(idx + 6) % 16]],
                        lst[cube3[(idx + 7) % 16]]])) == 1:
                continue
            else:
                break
        else:
            return True

        for idx in range(0, len(cube2), 4):
            if len(set([lst[cube3[idx]], lst[cube3[idx + 1]], lst[cube3[(idx - 1) % 16]],
                        lst[cube3[(idx - 2) % 16]]])) == 1:
                continue
            else:
                break
        else:
            return True
if check(cube1,cube2,lst):
    print(1)
else:
    print(0)