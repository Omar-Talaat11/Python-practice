

ls = [1,2,3,4,5,6,4,5,2,4] #list has 3 fours

count = 0

for i in ls:
    if i == 4:
        count+=1

print(f'the number of fours in the string = {count}')