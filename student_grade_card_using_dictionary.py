student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for key in student_scores:
  if student_scores[key]>=91:
    student_grades[key]="Outstanding"
  elif 91>student_scores[key]>=81:
    student_grades[key]="Exceeds Expectations"
  elif 81>student_scores[key]>=71:
    student_grades[key]="Acceptable"
  elif 71>student_scores[key]:
    student_grades[key]="Fail"
    
print(student_grades)
