## Class variables
- Shared among all of the class  
- Defined outside the constructor  
- Allow you to share data among all objects created fromt he class

```python
class Student:

  class_year = 2024 #class variabe
  student_num = 0 #class variable

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.student_num += 1

student1 = Student("Spongebob", 19)
student2 = Student("Patric", 20)

#print(f"{student1.name} is a {student1.age} years old student and will graduate in year {student1.class_year}.")
print(f"My graduating class of {Student.class_year} has {Student.student_num} students")
