### BlacKrab666 ###
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
        cls.displayEmployee
        cls.displayCount
        
    def displayCount(self):
        print(f"Total Employee {self.empCount}")
        
    def displayEmployee(self):
        print(f"Name : {self.name}", )
        
Employee.ojb1 = Employee("Mavrik") # even the only objectified code idea is thrown back into subjective reality
damn = Employee.obj1() # Not an object
# damn.displayEmployee()
# damn.displayCount()
print(damn)                     # <class '__main__.Employee'>
print(Employee)                 # <class '__main__.Employee'>
damn.ClassAssObjNotObj(damn)        # must follow up and see why statement is not printing but so far no errors. Jack not here.
Employee.ClassAssObjNotObj(damn)    # must follow up and see why statement is not printing but so far no errors. Jack not here.
print(Employee.obj1)            # <bound method Employee.obj1 of <class '__main__.Employee'>>
print(Employee.obj1())          # <class '__main__.Employee'>

# results show both ideas are the same, the projections of my mind minifest in reality with no objective reality
