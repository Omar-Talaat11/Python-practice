import os
import csv


return_types=['void', 'uint8', 'uint16', 'uint32' , 'uint64' , 'int8', 'int16', 'int32' , 'int64' , 'float' , 
              'double']
ID=0
file=open("gpio.h","r")
data=file.readlines()

filename="document_header"
file = open(filename,'w')
file.truncate(0)

writer=csv.writer(file)
frtype=""
fname=""

header_row=["Index","Return Type","Function Name","Argument_1","Argument_2","Argument_3","Argument_4"]
writer.writerow(header_row)
for line in data:
    # pass
    # print(line)
    arg_arr=[]
    word=line.split()
    try:
        if(word[0] in return_types):
            nword=word[1].split('(')
            nnword=(line.split('('))[1].split(',')
            frtype=word[0]
            fname=nword[0]
            # writer.writerow(frtype,fname)
            for arg in nnword:
                # print(arg.split(')')[0])
                arg_arr.append(arg.split(')')[0])
            print("-----------------")
            writer.writerow([f"IDX{ID}"]+[frtype,fname]+arg_arr)
            ID+=1
    except:
        pass
    
file.close()