N = int(input())
wordlist= []
seclist = []
for i in range(N):
    wordlist.append(input())
    seclist.append(wordlist[i]*2)
existcnt = 0
for i in range(0, N):
    cnt = 0
    for j in range(0, N):
        if (len(wordlist[i]) == len(seclist[j])/2) and (str(wordlist[i]) in str(seclist[j])):
            seclist[j] = ''
            cnt += 1
    if cnt > 0:
        existcnt += 1
print(existcnt)

# 맞았다!!!