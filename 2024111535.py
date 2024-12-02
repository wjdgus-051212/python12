assignment = int(input("과제 : "))
midterm = int(input("중간 : "))
final = int(input("기말 : "))

average = (assignment + midterm + final) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"평균 점수: {average:.8f}\n예상 학점: {grade}")
bmi = float(input("몸무게를 입력하세요: ")) / (float(input("키를 입력하세요: ")) ** 2)
print(f"BMI 지수 {bmi:.1f}")
