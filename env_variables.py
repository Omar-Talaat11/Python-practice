import os

ls = os.environ.items()
print('the environment variales available are:')

for key,value in ls:
    print(key,end=" ,")
else:
    print(".")

x=input('please enter the key for the environment you want\n')

print(os.environ[x.upper()])