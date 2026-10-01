l=[1,2,3,4,4,5,6,7,5]

# s=set(l)
# print(s)


ans=[]

for i in l:
    if i not in ans:
        ans.append(i)
print(ans)
     