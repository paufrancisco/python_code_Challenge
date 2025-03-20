class StudentQuizScore():
    
    student_status = False
   
    
    def get_info(self,PASSING_SCORE):    
        student_name = input("Enter the student name: ")
        student_age = int(input("Enter the student age: "))
        student_score = int(input("Enter the student score or press 0 if no quiz submitted yet: "))
        student_result = ""
        
        if student_score >= PASSING_SCORE:
            student_status = True
        elif student_score < PASSING_SCORE & student_score > 0:
            student_status = False
        elif student_score == 0:
            student_status = None
            
            
        if student_status:
            student_result = (f"{student_name} passed the exam")
        elif student_status == None:
            student_result = (f"{student_name} no quiz submitted yet")
        else:
            student_result = (f"{student_name} failed the exam")
            
        print(f"Student name: {student_name}")
        print(f"Student age: {student_age}")
        print(f"Student score: {student_score}")
        print(f"Student status: {student_result}")
    
        


student = StudentQuizScore()
student.get_info(5)
