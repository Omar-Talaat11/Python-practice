import os
import shutil



class Class_Data():
    def __init__(self,name,cname,namespace,cpp):
        self.name=name
        self.cname=cname
        self.namespace=namespace
        self.cpp=cpp
    
    
    
if(os.path.exists("project")):
    shutil.rmtree("project")
    print("Folder Deleted")
    
    
os.system("mkdir -p project")
os.system("touch project/Class.cpp")
os.system("touch project/Class.hpp")

name=input("Please enter your name\n")
cname=input("Please enter your class name\n")
namespace=input("Please enter your namespace\n")
cpp=input("Do you want cpp? Y/N \n")

my_class=Class_Data(name,cname,namespace,cpp)

f=open("project/Class.hpp","w")

f.write(f"#pragma once\n/**************************************\n*********** COPY RIGHT {my_class.name.upper()} ***********\n**************************************/\n\n")

f.write(f"namespace {my_class.namespace}\n")
f.write("{\n")
f.write(f"class {my_class.cname}")
f.write("{\n\n")
f.write("public:\n")
f.write(f"\t{my_class.cname}();\n")
f.write(f"\t~{my_class.cname}();\n")
f.write("private:\n\n")
f.write("};\n}")
f.close()

while 1:
    if(my_class.cpp=='Y'):
        file=open("project/Class.cpp","w")
        file.write(f"/**************************************\n*********** COPY RIGHT {my_class.name.upper()} ***********\n**************************************/\n\n")
        file.write('#include "Class.hpp"\n\n')
        file.write(f"namespace {my_class.namespace} \n")
        file.write("{\n")
        file.write(f"\t{my_class.cname}::")
        file.write(f"{my_class.cname}()")
        file.write("{}\n")
        file.write(f"\t{my_class.cname}::")
        file.write(f"~{my_class.cname}()")
        file.write("{}\n")
        file.write("}")
        break
    elif(my_class.cpp=='N'):
        os.system(f"rm project/{my_class.cname}")
        break
    else:
        cpp=input("Incorrect Value please enter Y/N\n")
        my_class.cpp=cpp

f.close()
    
    
    