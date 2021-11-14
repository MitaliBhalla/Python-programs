def change(n):
    if colour[n-1]=='w':
        colour[n-1]='b'
        q.append(n)
def source(n):
    if colour[n-1]=='b':
        colour[n-1]='r'
        '''for n in d:
            for j in d[n]:
                pre[j-1]=n
                dis[j-1]+=1'''
from collections import defaultdict
l=[]
n=int(input("enter no.of nodes"))
m=int(input("enter no.of edges"))

for i in range(m):
    
    x=input("enter edge")

    x=x.replace(",","")
    l.append(list(x))
s=int(input("enter source vertex"))

bfs=[]
d=defaultdict(list)

for i in l:
    d[int(i[0])].append(int(i[1]))
    d[int(i[1])].append(int(i[0]))
q=[]
colour=['w']*n
pre=[None]*n
dis=[0]*n

change(s)

for i in d[s]:

    change(i)


for i in d:
    change(i)
    for j in d[i]:
        change(j)

print(q)
while(len(q)!=0):
    element=q.pop(0)
    bfs.append(element)
    source(element)
    for i in d[element]:
        if colour[i-1]!='r':
            
            pre[i-1]=element
            dis[i-1]+=1

print(pre)
print(colour)
print(dis)
        


