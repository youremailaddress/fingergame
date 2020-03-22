def quchong(list1):
   list2=[]
   for l in list1:
       if l not in list2:
           list2.append(l)
   return list2

def getdata():
    bigdata = []
    for i in range (0,10):
        for j in range (0,10):
            for k in range (0,10):
                for m in range (0,10):
                    data = []
                    if i==0 and j==0:
                        data.append('NN')
                    
                    elif k==0 and m==0:
                        data.append('NN')
                    elif i==0 and j!=0:
                        if k == 0 and m != 0 :
                            data.append(str(i)+str((j+m)%10)+str(k)+str(m))
                        elif m == 0 and k != 0 :
                            data.append(str(i)+str((j+k)%10)+str(k)+str(m))
                        else:
                            data.append(str(i)+str((j+k)%10)+str(k)+str(m))
                            data.append(str(i)+str((j+m)%10)+str(k)+str(m))
                    elif i!=0 and j==0:
                        if k == 0 and m != 0 :
                            data.append(str((i+m)%10)+str(j)+str(k)+str(m))
                        elif m == 0 and k != 0 :
                            data.append(str((i+k)%10)+str(j)+str(k)+str(m))
                        else:
                            data.append(str((i+k)%10)+str(j)+str(k)+str(m))
                            data.append(str((i+m)%10)+str(j)+str(k)+str(m))
                    elif i!=0 and j!=0:
                        if k == 0 and m != 0 :
                            data.append(str((i+m)%10)+str(j)+str(k)+str(m))
                            data.append(str(i)+str((j+m)%10)+str(k)+str(m))
                        elif m == 0 and k != 0 :
                            data.append(str((i+k)%10)+str(j)+str(k)+str(m))
                            data.append(str(i)+str((j+k)%10)+str(k)+str(m))
                        else:
                            data.append(str((i+k)%10)+str(j)+str(k)+str(m))
                            data.append(str((i+m)%10)+str(j)+str(k)+str(m))
                            data.append(str(i)+str((j+k)%10)+str(k)+str(m))
                            data.append(str(i)+str((j+m)%10)+str(k)+str(m))
                    data = quchong(data)
                    bigdata.append(data)
    return bigdata

def fuc(n,num):
    if num !='NN':
        for t in range(0,len(bigdata[int(num)])):
            c = n
            c-=1
            if c > 0:
                fuc(c,bigdata[int(num)][t][::-1])
            else:
                for s in range (0,len(bigdata[int(num)])):
                    smalldata.append(bigdata[int(num)][s][::-1])
                return smalldata
        n -=1
    
def count(lis):
    co = 0
    for li in lis:
        if li[2:4] == '00':
            co += 1 
    return co


def winornot(d,y):
    win = 1
    lose = 1
    for q in range(1,11):
        fuc(q,d[y])
        f = smalldata[:]
        smalldata.clear()
        if q % 2 == 1:
            lose += count(f)
        if q % 2 == 0:
            win += count(f)
    return win/lose

def cl(listw,nc):
    for i in range(0,len(listw)):
        if listw[i] == nc :
            return i


def run():
    x = input('Please input nums:')
    x = x[::-1]
    winstuff = []
    for y in range (0,len(bigdata[int(x)])):
        fuc(1,x)
        d = smalldata[:]
        smalldata.clear()
        g = winornot(d,y)
        winstuff.append(g)
    fuc(1,x)
    d = smalldata[:]
    smalldata.clear()
    print(d[cl(winstuff,max(winstuff))])

while True:
    bigdata = getdata()
    smalldata = []
    run()