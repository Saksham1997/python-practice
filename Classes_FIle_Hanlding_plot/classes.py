# Python OOPS
#classes and instances
#incorporating file handling and plotting line graphs also

"""
functionalities to be added includes :
1. update file contents
2. after updating the files plotting the graph
3. Error handling to check the name of the employee is present in the object list when we are updating its pay
"""
import matplotlib.pyplot as plt

class Employee:
  num_employee_trading=0
  num_employee_clearing=0
  num_employee_IFSC=0
  raise_amount = 1.04 #class variable
  def __init__(self, first, last, pay, dept):
      self.first=first
      self.last=last
      self.pay=float(pay)
      self.email= first + '.' + last + '@company.com'
      self.dept=dept
      if(self.dept == 'Trading'):
          Employee.num_employee_trading+=1 #class variable
      elif(self.dept == 'Clearing'):
          Employee.num_employee_clearing+=1
      elif(self.dept == 'IFSC'):
          Employee.num_employee_IFSC+=1
  def fullname(self):
      return("Your name is {} {}".format(self.first,self.last))

  def self_raise(self):
      self.pay = float(self.pay * Employee.raise_amount) #to access the class variable , we need to add class name or instance name like : self.variable

  @classmethod
  def self_raise_amt(cls,amount):
      cls.raise_amount = amount

def Plot_it(x_axis,y_axis):
    name_file=input("Enter the image filename")
    type=input("Enter the type of plot to be created (scatter/histogram/line) ")
    if type.lower()=='scatter':
        plt.scatter(x_axis,y_axis)
        plt.yscale('log')
    elif type.lower()=='histogram':
        plt.hist(y_axis,bins=20)
    elif type.lower()=='line':
        plt.plot(x_axis,y_axis)
    plt.grid(True)
    plt.title("Salary Comparision")
    plt.xlabel('Name')
    plt.ylabel('Pay')
    plt.pause(0.1)
    plt.savefig(name_file)

"""
#self keyword takes whole object
emp1= Employee('Saksham','Singhal',60000,'Trading')
emp2= Employee('Akanshya','Dash',60000,'Clearing')

print(emp1.email)
print(emp2.email)
"""
"""
#passing functions to object , self keyowrd takes the attribute of the object
print(emp1.fullname())
print(emp2.fullname())

#passinf functions to a class
Employee.fullname(emp1)
Employee.fullname(emp2)

print(emp1.pay)
emp1.self_raise()
print(emp1.pay)
Employee.self_raise_amt(10)
emp2.self_raise()
print(emp2.pay)
print(emp1.__dict__)
print(Employee.num_employee_trading,Employee.num_employee_clearing)
"""


#USING FILEHANDLING AND CLASSES TOGETHER
fname=input("Enter filename")
try:
    fhandle=open(fname,'r')
except:
    print("The file %s doesnt exist" % fname)
    quit()
lis=[]
for line in fhandle:
    first,last,pay,dept=line.split(',')
    var=Employee(first,last,pay,dept)
    lis.append(var)
fhandle.close()
#LOOP TO FIND MAXIMUM PAY
max_pay=0
Names=[]
Pay=[]
for obj in lis:
    print(obj.first,obj.last,obj.pay,obj.dept,obj.email)
    Names.append(obj.first)
    Pay.append(obj.pay)
    if (int(obj.pay) > int(max_pay)):
        max_pay=obj.pay
        emp_name=obj.first

print("The highest salary employee name is {} and the salary is {}".format(emp_name,max_pay))
print("\n Names:{} \t Pay:{}".format(Names,Pay))
Plot_it(Names,Pay)


#FIND THE EMPLOYEE FOR WHICH PAY HAS TO BE INCREASED AND INCREASING IT BY TAKING USER INPUT
check=input("Do you want to update anyone's pay (Press y/Y/N/n)?")
if check.lower() == "n":
    pass
elif check.lower() == "y" :
    updated_Name=[]
    updated_pay=[]
    name_pay=input("Enter the name of the employee")
    for obj in lis:
        try:
            if(obj.first == name_pay):
                #old_pay = obj.pay
                pay_increase=float(input('Enter the increase to be given'))
                Employee.self_raise_amt(pay_increase)
                Employee.self_raise(obj)
                print("\n Name:{} \t Pay:{}".format(obj.first,obj.pay))
        except:
            print('name doesnt exist')
        updated_Name.append(obj.first)
        updated_pay.append(obj.pay)

Plot_it(updated_Name,updated_pay)
