class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.gender = new_gender
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        """回傳private屬性"""
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.gender = new_gender
        else:
            print('====請輸入"M"或"F"====')
    def borrow_resources(self):
        print('someone borrow')


class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def join_class(self):
        pass

    def quit_class(self):
        pass

    def borrow_resources(self):
        print('student borrow')

class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('professor borrow')

studentA = Student('M', '工管系', 'M10821003')
studentB = Student('F', '工管系', 'M10822503')
professorA = Professor('M', '氣管系', 'T1056')
professorB = Professor('F', '資工系', 'T1082')

ls = [studentA, studentB, professorA, professorB]

from item in ls:
     item.borrow_resources()
