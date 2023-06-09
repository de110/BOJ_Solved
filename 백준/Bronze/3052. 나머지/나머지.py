data=[]
for i in range(10):
    a=int(input())%42
    if a not in data:
        data.append(a)
        
print(len(data))