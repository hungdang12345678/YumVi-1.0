class Person:
    name = str
    _age = int
    
    def _init_(self, name, age):
        self.name = name
        self._age = age
    def _str_(self):
        return "Tên %s, Tuổi: %d" % (self.name, self._age)
    
    def say_hello(self):
        print("Xin chào, tên %s tuổi %d " % (self.name, self._age))
class Student(Person):
    _studentId = int

    def _int_(self, name, age, studentId):
        super()._int_(name, age)
        self._studentId = studentId

    def _str_(self):
        return super()._str_() + "MSV: %d" % (self._stuentId)
    
    def get_student_id(self):
        return self._studentId
    
    def set_student_id(self, studentId):
        self._studentId = studentId