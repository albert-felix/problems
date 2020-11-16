class Parse:

    def __init__(self,name,clgName,address):
        self.name = name
        self.clgName = clgName
        self.address = address
    
    def enroll(self):
        print(f"{self.name} is enrolled for the PARSE course")
    
    def attendance(self,num):
        self.attendance = num
    

    def assignment(self,marks):
        self.a_marks = marks
    
    def exam_marks(self,marks):
        self.e_marks = marks

    def final_marks(self):
        self.f_marks = self.a_marks + self.e_marks
        print(f"Final Marks : {self.f_marks}")

    def display(self):
        print(f"Overall Grade : {self.f_marks}")
        print(f"Name : {self.name}")
        print(f"Assignment Marks : {self.a_marks}")
        print(f"Exam Marks : {self.e_marks}")
        print(f"Attendance : {self.attendance}")

        
albert = Parse('Albert', 'ABC College', 'Chennai')
albert.enroll()
albert.attendance(30)
albert.assignment(10)
albert.exam_marks(80)
albert.final_marks()
albert.display()
