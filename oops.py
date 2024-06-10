# class circle : 
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         area = 3.14 * pow(self.radius,2)
#         print(area)

#     def perimeter(self):
#         peri = 2*3.14*self.radius
#         return peri
    
# c1 = circle(10)
# c1.area()
# print(c1.perimeter())
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def display(self):
        print(self.role)
        print(self.department)
        print(self.salary)

# emp = Employee("sdet","cs",40000)
# emp.display()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("chatgpt","it","50000")
        super().display()

    def display1(self):
        
        print(self.name)
        print(self.age)
eng = Engineer("sahil",22)
eng.display1()

