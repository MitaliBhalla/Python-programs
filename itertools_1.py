from itertools import permutations
s="abcdef"
res=[]
l=list(permutations(s))
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        res.append(s[i:j])
print(res)
x=123%10
re=123//10
re=re*10+x
print(re)


# repeat() 
     
# importing "itertools" for iterator operations 
import itertools 
     
# using repeat() to repeatedly print number 
print (list(itertools.repeat(25, 4)))
