ch = input("please enter a character\n")
while 1:
    print(f"the ascii for {ch} is {ord(ch)}")
    ch=input("enter another letter or 0 to end\n")
    if(ch=='0'):
        break
print("thank you")