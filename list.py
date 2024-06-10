student = ["sahil", 22, "Amey", 23, "pranav", 27]
student.append("Anil")
print(student)
student.insert(2,"kumar")
print(student)
student.remove("sahil")
print(student)
student.pop(1)
print(student)

list1 = [1,2,1]
list2 = list1.copy()
list2.reverse()
print(list2)
if(list2==list1):
    print("palindrome ")
else:
    print("not")

print(list2.count("sahil"))