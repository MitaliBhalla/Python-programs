s="intell#ect"
l=list(s)
count=0
for i in s:
    if (i.isalpha())==False and (i.isnum())==False:
        count+=1
print(count)
