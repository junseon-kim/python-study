# 2019.12.25 오늘은 원래 안하려고 했지만 백준을 풀다가 리스트 관련 함수가 계속 나와서 짧지만 정리.
alist = []
for i in range(1, 11):
    alist.append(str(i))
else:
    print(alist)
bstr = 'abc'.join(alist) # join은 리스트를 붙이는 기능을 함. 반환문자열 = '리스트값 사이사이에 들어갈 문자열'.join(변환할리스트)
print(bstr)

clist = bstr.split('b') # split은 문자열을 리스트로 나누는 역할. 반환리스트 = 나눌문자열.split('나누는기준문자열')
# 나누는 기준이 되는 문자열은 리스트에서 빠지게 된다. split()에 아무것도 없으면 띄어쓰기로 구분한다.
print(clist)


dstr = bstr[:] # 문자열을 slicing 하면 문자열로,
print('slice1', dstr)
dstr = bstr[:].split('abc') # 문자열을 슬라이싱하고 바로 리스트로 split할 수도 있을까?
print('slice2', dstr)


elist = clist[1:5] # 리스트를 slicing 하면 리스트로.
print('slice3', elist)
fstr = ' JOIN '.join(clist[1:5]) # slicing한 것을 바로 join하면 문자열로.
print('slice4', fstr)
gstr = ''.join(fstr.split())
print('splt, join', gstr)

print('리스트의 슬라이싱을 이용한 삭제, 수정')
hlist = alist[:]
print(hlist)
hlist[1:5] = 'deleted' # 리스트 하나에 문자열이 전부 들어가는 것이 아니라 문자 하나하나 나눠서 [1:5]에 들어간다.
# 즉, [1:5]를 없애고 그곳에 넣고싶은 것을 넣을 수 있다는 얘기.
print('1', hlist)
ilist = alist[:]
print(ilist)
ilist[1:5] = 'T'
print('2', ilist)

jlist = alist[:]
jlist[1:5] = ['deleted', 'inserted'] # 리스트를 넣으면 문자열 하나하나가 한 칸에 전부 들어간다.
print('3', jlist)

# 오늘의 예상외의 파이썬 종료.