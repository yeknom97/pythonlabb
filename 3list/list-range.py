num=list(range(5,0,-1))
print(num)

num[2]=100
print(num)

a=[1,2,3]
total=0
for el in a:
    total+=el
total2=sum(a)
print(total,total2)

b= range(5,0,-1)
#b= range[5,4,3,2,1]
total3=sum(b)
print(total3)

#stra="stone"
#stra[a]="y"
#print(stra)
stra="stone"
stra=list(stra)
stra[0]="y"
print(stra)
print(','.join(stra))
