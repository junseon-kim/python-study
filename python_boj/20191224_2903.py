# 점을 찍는데, 중복되는 점은 빼고 찍는다. 규칙을 보면, 제곱수 라는 것을 알 수 있다. 제곱수를 구해보자. N=1, result=4
# N=0 > res=4, N=1 > res=9, N=2 > res=25 이전 한 변의 점의 개수 -1 개가 증가한다.
N = int(input())
dot = [4]
line = 2
for i in range(0, N):
    line = line+line-1
    dot.append(line**2)
print(dot[N])
