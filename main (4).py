class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name 
    self.roll_number=roll_number
    self.cgpa=cgpa 
def sort_students(student_list):
    sorted_students=sorted (student_list, key=lambda student:student.cgpa,reverse=True)
    return sorted_students


students=[
      student(" hari","A123",7.8),
      student("sri","A122",8.9),
      student("mani","A124",9.1)]

sorted_students=sort_students(students)
for student in sorted_students:
  print("name: {},roll_number: {},cgpa: {}". format(student.name,
student.roll_number,
student.cgpa))
    