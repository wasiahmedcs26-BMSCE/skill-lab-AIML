import numpy as np
std_score=np.array([
    [35,33,38,29,31],
    [48,47,43,44,42],
    [18,21,17,15,19],
    [25,21,26,27,24],
    [30,35,32,37,33],
    [45,47,48,50,44],
    [15,11,13,18,12]
])
print(std_score)
print("Student 7 , sub 2 is",std_score[6,1])

def marks(student,sub):
    student=int(student)
    sub=int(sub)
    print(f"student {student} Scored {std_score[student-1,sub-1]} in Subject {sub}")
# student=input("Enter student number")
# sub=input("Enter Subject number")


# marks(student,sub)

print("Studnet 3, sub 2,3,4 :", std_score[2,1:4])
print("All students, sub 2,3,4" , std_score[:,1:4])
total_score=np.sum(std_score,axis=1)
avg_score=np.mean(std_score,axis=1)
print("Total score of each student",total_score)
print("Average score of each student",avg_score)

#highest makrs in each subject 
highest_marks=np.max(std_score,axis=1)
print("Highest marks in each subject",highest_marks)