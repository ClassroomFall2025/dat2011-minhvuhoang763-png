
class SinhVienPoly:
    def __init__(self, ho_ten, nganh, diem):
        self.__ho_ten = ho_ten
        self.__nganh = nganh
        self.__diem = diem

    def get_diem(self):
        return self.__diem

    def get_hoc_luc(self):
        if self.__diem < 5:
            return "Yếu"
        elif self.__diem < 7:
            return "Trung bình"
        elif self.__diem < 8:
            return "Khá"
        elif self.__diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ tên: {self.__ho_ten}")
        print(f"Ngành: {self.__nganh}")
        print(f"Điểm: {self.__diem:.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")
