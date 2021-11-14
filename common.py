s1='jfiowj'
s2='jvoeljg0pwp'
for i in s1:
    if i in s2:
        s1=s1.replace(i,"",1)
        s2=s2.replace(i,"",1)
print(len(s1)+len(s2))
