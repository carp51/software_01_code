#開発者作成部分
def getMax(a):
    amax = a[0]
    aindex = 0
    for j in range(1, len(a)):
        #print(a[j])
        if a[j] > amax:
           amax = a[j]
           aindex = j
    return (amax, aindex)

#ユーザ利用部分
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bm = getMax(b)
print('max=', bm[0])

