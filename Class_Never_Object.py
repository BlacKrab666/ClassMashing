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
        
Employee.ojb1 = Employee("Mavrik")
damn = Employee.obj1()
# damn.displayEmployee()
# damn.displayCount()
print(damn)
print(Employee)
damn.ClassAssObjNotObj(damn) # must follow up and see why statement is not printing but so far no errors. Jack not here.
