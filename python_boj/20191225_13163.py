# N = int(input())
# for i in range(0, N):
#     strs = input()
#     strs = strs.split()
#     strs[0] = 'god'
#     resstr = ''
#     for j in range(0, len(strs)):
#         resstr = resstr + strs[j]
#     print(resstr)


# 위의 것으로 제출했고, 지금은 새로 배운 join을 활용해보자.
N = int(input())
for i in range(0, N):
    strs = input().split()
    strs[0] = 'god'
    resstr = ''.join(strs)
    print(resstr)
