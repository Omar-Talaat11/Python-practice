ls = [1,3,4,5,6,7,8,9,1,2,3,4,2,55,6,1,2,4,5]

mx= ls[0]

for i in ls:
    if mx<i:
        mx=i
        
print(f'maximum is {mx}')