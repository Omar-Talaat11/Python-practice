import os
import shutil

if(os.path.exists("project")):
    shutil.rmtree("project")
    print("Folder Deleted")

os.system("mkdir -p project/src")
os.system("touch project/src/GPIO_init.c")

ports=['A','B','C','D']

f=open("project/src/GPIO_init.c","w")

f.write("void GPIO_Init(void)\n{\n")


Values=[]


print("please enter the value of 1 for output and 0 for input")
for P in ports:
    Port=[]
    for i in range(8):
        Port.append(input(f"please enter Port {P} pin {i}\n"))
    Values.append("".join(Port))

y=0
for P in ports:
    # for i in range(8):
    f.write(f"\tDDR{P}=0b{Values[y]}\n")
    f.write("\\\\\\\\\\\n")
    y+=1
        
f.write("}")
f.close()