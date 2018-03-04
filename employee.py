def add_emp():
    id=0
    details=[]
    n=input("Please enter the number of records you wish to add")
    while(n):
        id=id+1
        print("Please enter the following details to add the employee")
        name=input("Enter the name of employee")
        dob=input("Enter the DOB of the employee")
        address=input("Enter the address of the employee")
        sal=input("Enter the salary of the employee")
        n-=1
        d1=insert(name,dob,address,sal,details)
    display(d1)
    search(d1)   
    delete(d1)    
        

def display(d1):
    print("-------------------------------------")
    
    print("Display the employee data")
    print d1
            

def insert(name,dob,address,sal,details):
    
    details.append({'Name':name,'DOB':dob,'Address':address,'Salary':sal})
    
    return details

        
def search(d1):
    
    input1=input("Enter the name field to search")
    for i in range (len(d1)):
        if(input1== d1[i]['Name']):
            print d1[i]
    

def delete(d1):
    
    i1=input("Enter the name to be deleted")
    for i in range (len(d1)):
        if(i1== d1[i]['Name']):
            
            del d1[i]
    print d1[i]
            

if(__name__=="__main__"):
    print("Employee Enrollment")
    print("1:To add employee details")
    print("2:Search employee")
    print("3.Delete employee")
    print("4.Modify employee")
    i1=input("Enter your choice")
    if(i1 == 1):
        add_emp()
#    if(i1== 2):
#        search()
     
