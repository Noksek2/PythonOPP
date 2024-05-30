class Student():
    def __init__(self,name):
        self.name=name
        print('Student : ',self.name)
    def __del__(self):
        print('Student', self.name,'객체 삭제')

class Teacher():
    def __init__(self):
        print('Teacher 객체 생성')
        self.stu1=Student('Joe')
        self.stu2=Student('Arm')
        self.stu3=Student('Park')
    def __del__(self):
        print('Teacher 객체 삭제')
teac=Teacher()
del teac
