class CanBo:
    def _init_(self, name='', age=0, gender='', address=''):
        self.name = name
        self.age = age
        self.gender = gender
        self.address= address

    def _str_(self):
        return f"Họ và tên: {self.name}\nTuổi:{self.age}\nGiới Tính:{self.gender}\nĐịa Chỉ:{self.address}"
    
    def themmoi_cb(self):
        self.name = input("Nhập vào họ tên:")
        self.age = input("Nhập vào tuổi:")
        self.gender = input("Nhập vào giới tính:")
        self.address = input("Nhập vào địa chỉ:")

class CongNhan(CanBo):
    def _init_(self, name='', age=0, gender='', address='', level=0):
        super()._init_(name, age, gender, address)
        self.level = level

    def _str_(self):
        return super()._str_() +f"\nBậc:{self.level}"
    def themmoi_cb(self):
        super().themmoi_cb()
        self.level = input("Nhập vào bậc:")

class KySu(CanBo):
    def _init_(self, name='', age=0, gender='', address='', major=''):
        super()._init_(name, age, gender, address)
        self.major = major

    def _str_(self):
        return super()._str_() +f"\nChuyên ngành: {self.major}" 

    def themmoi_cb(self):
       super().themmoi_cb()
       self.major = input("Nhập vào chuyên ngành")

class NhanVien (CanBo):
    def _init_(self, name='', age=0, gender='', address='', task=''):
        super()._init_(name, age, gender, address)
        self.task = task
        
    def _str_(self):
        return super()._str_() +f"\n Công việc:{self.task}"
    def themmoi_cb(self):
        super().themmoi_cb()
        self.task = input("Nhập vào công việc:")

class QLCB:

    def add_cb(self):

        n=int(input("Nhập vào số người:"))
        danhsach_cb =[]
        for i in range (n):
            choise = int(input("Nhập vào 1/Công nhân, 2/Kỹ sư, 3/Nhân viên:"))
            if choise ==1:
                person = CongNhan()
                person.themmoi_cb()
            elif choise == 2:
                person = KySu()
                person.themmoi_cb()
            elif choise ==3:
                person = NhanVien()
                person.themmoi_cb()
            else: print ("Nhập sai!")
            danhsach_cb.append(person)
        return danhsach_cb
    def hienthi_cb(self,danhsach):
        for s in danhsach:
            print(s)
    
    def timkiem_cb(self,danhsach):
        find_name = input("Nhập vào tên bạn muốn tìm:")
        for s in danhsach:
            s.name = find_name 
            print(s)
        else: print("Không có!")
    
danhsach = QLCB() .add_cb()

QLCB().hienthi_cb(danhsach)
