m = ["john","johnny","jackie","johnny","john","jackie", "jamie","jamie","john","johnny","jamie","johnny", "john"]
l={}
p=[]
x=0
for i in m:
    l[i]=m.count(i)
    r=m.count(i)
    if r>x:
        x=r
for i in l:
    if l[i]==x:
        p.append(i)
p.sort()
print(p[0])




    
