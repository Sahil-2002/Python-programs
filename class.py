class student:
    def __init__(self,name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self):
        avg = (self.mark1+self.mark2+self.mark3)/3
        return avg
        



student1 = student("Sahil", 1,2,3)

# Accessing methods of the student object
print(student1.avg())
