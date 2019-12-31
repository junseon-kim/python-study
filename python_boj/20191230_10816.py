# 숫자카드 N개, 정수, 찾을 개수 M개, 정수

#  N 개의 리스트 생성.
N = int(input())
Ncntdict = {}  # 시간초과로 인해 딕셔너리의 키를 이용하여 풀기로 함.
Nlist = list(map(int, input().split()))  # 일단 가진 정수를 받는다.
for i in range(N):
    if Nlist[i] not in Ncntdict:  # 키가 존재하지 않는다면,
        Ncntdict[Nlist[i]] = 0  # 해당 키를 생성, 0을 할당한다.
    Ncntdict[Nlist[i]] += 1  # 키가 있다면, 1을 올린다.
M = int(input())  # 구할 카드의 개수를 받는다.
Mlist = list(map(int, input().split()))  # 구할 정수를 받는다.
Mcntlist = []  # 개수를 넣을 리스트를 만든다.
# Mcntstr = ''
for i in range(len(Mlist)):  # 다시 보니 range(M)으로 써도 된다. 바보였다.
# for i in range(M):
    if Mlist[i] in Ncntdict:  # 이것 또한 키가 있으면 해당 키의 밸류 +1 시킨다.
        Mcntlist.append(str(Ncntdict[Mlist[i]]))
        # Mcntstr += str(Ncntdict[Mlist[i]])
    else:
        Mcntlist.append('0')  # 없다면 0을 넣는다.
    #     Mcntstr += '0'
    # if i < M-1:
    #     Mcntstr += ' '
else:
    print(' '.join(Mcntlist))  # join은 str로 된 list만 되는 것 같다.
    # print(Mcntstr)

# str보다 list로 계산한 것이 더 빠르다. str은 if와 연산이 조금 더 많기 때문인가?
# list에서 join을 쓴 것이 972ms, 곧바로 str을 구한 것이 1132ms 걸렸다.
# 결론 : 연산이 많이 반복되는 코드에서는 if문 하나, 연산 하나가 시간 지연의 이유가 된다.
