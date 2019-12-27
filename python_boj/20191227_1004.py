# def indis(x1, y1, st):
#     disx = (x1-st[0])**2
#     disy = (y1-st[1])**2
#     if disx+disy > st[2]**2:
#         return False
#     elif disx+disy < st[2]**2:
#         return True
#
#
# T = int(input())
# for i in range(T):
#     sx, sy, ex, ey = map(int, input().split())
#     cnt = 0
#     n = int(input())
#     for j in range(n):
#         star = list(map(int,input().split()))
#         if indis(sx, sy, star) != indis(ex, ey, star):
#             cnt += 1
#     else:
#         print(cnt)

# 맞았다. 나의 생각을 정리해보자
'''
1. 경로를 하나하나 구해야하나?
2. 내 수준에서 그게 가능한가?
3. 아니다. 이건 더 쉽게 풀 수 있다.
4. 시작점과 끝점이 원 안에 들어간 횟수만 구하면 되나?
5. 아니다. 유심히 행성도를 보자.
6. 보면서 생각하니, 이건 최소 거리도 아니고 출입 횟수를 구하는 것이다.
7. 그러므로 경로를 구할 것까지는 없을 것이다.
8. ? 그럼 출입만 구하면 되나?
9. 출입이 없는 경우는 
    9-1 둘이 같은 원 안에 있을 경우
    9-2 둘이 같은 원 안에 없을 경우
10. 출입이 있는 경우는 하나라도 같은 원 안에 있거나 없을 경우이다.

결론 : 시작점과 끝점이 원 안에 있는지만 구해서 비교, 둘이 다르면 횟수를 올린다.
결과 : 맞음.
'''


# 축약해보자.
def indis(x1, y1, st):
    dis = (x1-st[0])**2 + (y1-st[1])**2
    if dis > st[2]**2:
        return False
    elif dis < st[2]**2:
        return True


for i in range(int(input())):
    pt = list(map(int, input().split()))
    cnt = 0
    for j in range(int(input())):
        star = list(map(int, input().split()))
        if indis(pt[0], pt[1], star) != indis(pt[2], pt[3], star):
            cnt += 1
    else:
        print(cnt)
# 16줄로 줄였다.