class Employee:
    name = 'Jack'
    empCount = 0
    obj1 = any([])
    
    def __init__(self, name):
        self.name = name
        Employee.empCount += 1
    
    @classmethod
    def obj1(cls):
        return cls
    
    def ClassAssObjNotObj(cls):
        cls.displayEmployee(cls)
        cls.displayCount(cls)
        
    def displayCount(self):
        print(f"Total Employee {self.empCount}")
        
    def displayEmployee(self):
        print(f"Name : {self.name}", )
        
Employee.ojb1 = Employee("Mavrik")
damn = Employee.obj1()
damn.displayEmployee(damn)
damn.displayCount(damn)
print(damn)
print(Employee)
damn.ClassAssObjNotObj(Employee)
Employee.ClassAssObjNotObj(damn)
print(Employee.obj1)
print(Employee.obj1())


#---------------------------------------------------------------------
### Output ###
# Name : Jack
# Total Employee 1
# <class '__main__.Employee'>
# <class '__main__.Employee'>
# Name : Jack
# Total Employee 1
# Name : Jack
# Total Employee 1
# <bound method Employee.obj1 of <class '__main__.Employee'>>
# <class '__main__.Employee'>
#=====================================================================

