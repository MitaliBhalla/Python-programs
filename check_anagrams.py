s1='abcd'
s2='kafc'
count=0
if len(s1)!=len(s2):
    print("no")
else:
    for i in s1:
        if i not in s2:
            count+=1
    if count==0:
        print("yes")
    else:
        print("no")
            
    
