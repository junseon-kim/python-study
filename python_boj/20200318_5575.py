def calctime(ti):
    first = ti[3]-ti[0]
    sec = ti[4] - ti[1]
    thi = ti[5] - ti[2]
    if thi >= 60:
        thi -= 60
    elif thi < 0:
        thi += 60
        sec -= 1
    if sec >= 60:
        sec -= 60
    elif sec < 0:
        sec += 60
        first -= 1
    if first>=24:
        first -=24
    elif first<0:
        first+=24
    return print(first, sec, thi)

time = []
for i in range(3):
    time = list(map(int, input().split()))
    calctime(time)