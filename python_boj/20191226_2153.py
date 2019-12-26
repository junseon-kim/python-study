# prime number string
# prmstr = list(input())
# prmcnt= 0
# for i in range(len(prmstr)):
#     if (prmstr[i] >= 'a') & (prmstr[i] <='z'):
#         prmcnt = prmcnt + (ord(prmstr[i]) - 96)
#     elif (prmstr[i] >= 'A') & (prmstr[i] <='Z'):
#         prmcnt = prmcnt + (ord(prmstr[i]) - 38)
# isprime = 0
# for i in range(2, prmcnt):
#     if not(prmcnt % i):
#         isprime += 1
# if isprime == 0:
#     print('It is a prime word.')
# else:
#     print('It is not a prime word.')

# 새로 배운 것 : 위의 방식은 기본적인 소수 접근법. 추가로 에라토스테네스의 접근법을 설명.
# 에라토스테네스의 접근법 : N을 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문.
# 밑은 위의 방법을 적용하여 첫 번째 시도를 고친 것이다.
prmstr = list(input())
prmcnt= 0
for i in range(len(prmstr)):
    if (prmstr[i] >= 'a') & (prmstr[i] <='z'):
        prmcnt = prmcnt + (ord(prmstr[i]) - 96)
    elif (prmstr[i] >= 'A') & (prmstr[i] <='Z'):
        prmcnt = prmcnt + (ord(prmstr[i]) - 38)
isprime = 0
for i in range(2, prmcnt**0.5 + 1): # 제곱근 이하이기 때문에 제곱근 +1을 해준다.
    if not(prmcnt % i):
        isprime += 1
if isprime == 0:
    print('It is a prime word.')
else:
    print('It is not a prime word.')

# 밑의 것은 같은 파이썬으로 짠 ryuwhale95 님의 코드이다. 너무 충격적이라서 가져왔다. 초보자는 할 수 없는 형태의 코딩인 것 같다.
# 이 밑의 코드는 내가 짠 것이 아니다.
# d={chr(65+i):27+i for i in range(26)} 아까 배운 Dict 타입. 키 값과 밸류를  for문을 써서 초기화를 할 수 있다.
# d.update({chr(97+i):1+i for i in range(26)})
# s=sum([d[i]for i in input()]) sum()은 리스트의 합을 구하는 것 같다. 리스트도 for문을 써서 할당할 수 있구나.
# f=True
# for i in range(2,int(s**0.5)+1): 이 줄을 보고 소수의 조건을 검색해보고 위의 에라토스테네스의 접근법을 보았다.
#     if s%i==0: f=False;break
# print("It is "+['not ',""][f]+"a prime word.") 문자열에도 조건을 붙일 수가 있다.

# 파이썬은 내 생각보다 더욱 크다는 것을 알게 된 날이다.