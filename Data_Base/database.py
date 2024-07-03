import csv
Data_Base=[]
class Employee:
    name=""
    job=""
    salary=0
    id=0
    def __init__(self,name,job,salary,id):
        self.name=name
        self.job=job
        self.salary=salary
        self.id = id
    
    def print_data(self):
        print(f"Employee's name: {self.name}\nPosition: {self.job}\nSalary: {self.salary}\nID: {self.id}")
    
    def update_employee(self,njob,nsalary):
        self.job=njob
        self.salary=nsalary
    


    
    
def Write_Data_Base():
    file=open("Employees_Data_Base.csv","w")
    file.truncate(0)
    writer=csv.writer(file)
    header_row=["Employee Name","Job","Salary"]
    writer.writerow(header_row)
    i=0
    for Emp in Data_Base:
        writer.writerow([Emp.name,Emp.job,int(Emp.salary)])
    file.close()
    
    
def Add_Employee(name,job,salary):
    nid=len(Data_Base)+1
    nEmployee=Employee(name,job,salary,nid)
    Data_Base.append(nEmployee)
    
def Read_Data_Base():
    file=open("Employees_Data_Base.csv","r")
    file.readline()
    data=file.readlines()
    i=0
    for line in data:
        word=line.split(',')
        Add_Employee(word[0],word[1],word[2])
    file.close()
    
def Del_Employee(id):
    i=0
    for Emp in Data_Base:
        if(Emp.id==id):
            del Data_Base[i]
            return
        i+=1
    print("Sorry ID not found")

def Print_Employee(id):
    for Emp in Data_Base:
        if(Emp.id==id):
            Emp.print_data()
            return
    print("Sorry ID not found")

def Display_DataBase():
    if(len(Data_Base)==0):
        print("Database is still empty")
        return
    for Emp in Data_Base:
        print(f"*********************")
        Emp.print_data()
        
def Update_Employee(id,job,salary):
    for Emp in Data_Base:
        if(Emp.id==id):
            Emp.update_employee(job,salary)
            print("Employee Updated:")
            Emp.print_data()
            return
        
    print("Sorry ID not found")
# Add_Employee("omar","eng",1000)
# Add_Employee("ahmed","dr",2000)
# Add_Employee("laila","busi",3000)

# Del_Employee(1)
# Display_DataBase()

print("Welcome to the Employees DataBase!!\nHere is the list of the available options")
Read_Data_Base()
while 1:
    print("************************\n1-Add a new employee")
    print("2-Remove an employee")
    print("3-Print an employee data")
    print("4-Display the data and IDs of all employees")
    print("5-Update an Employee Data\n")
    x=int(input("or Enter 0 to end\n"))
    
    if(x==1):
        name=input("please enter name of the employee\n")
        job=input("please enter job of the employee\n")
        salary=input("please enter salary of the employee\n")
        Add_Employee(name,job,salary)
        print("Employee Successfully added to the Database")
    elif(x==2):
        did=int(input("please enter the employee's ID\n"))
        Del_Employee(did)
    elif(x==3):
        pid=int(input("please enter the employee's ID\n"))
        Print_Employee(pid)
    elif(x==4):
        Display_DataBase()
    elif(x==5):
        uid=int(input("please enter the employee's ID\n"))
        ujob=input("please enter job of the employee\n")
        usalary=input("please enter salary of the employee\n")
        Update_Employee(uid,ujob,usalary)
    elif(x==0):
        print("Thank You!!")
        Write_Data_Base()
        break
        
        
        
        
    




