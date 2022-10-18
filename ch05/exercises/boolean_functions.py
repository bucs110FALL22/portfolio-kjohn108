def percentage_to_letter(score=0):
  if(score > 90) or (score == 90):
    grade = "A"
  elif(score < 90) and (score >= 80):
    grade = "B"
  elif(score < 80) and (score >= 70):
    grade = "C"
  elif(score < 70) and (score >= 60):
    grade = "D"
  elif(score < 60):
    grade = "F"
  return grade

score = float(input("student score: "))
letter_grade =percentage_to_letter(score)

def is_passing(grade):
  if (grade == "A") or (grade == "B") or (grade == "C"):
    return True
  else:
    return False

print(letter_grade)
print(is_passing(letter_grade))