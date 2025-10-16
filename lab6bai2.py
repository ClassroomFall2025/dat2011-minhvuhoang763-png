from abc import ABC, abstractmethod

class SinhVienPoly(ABC):
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh

    @abstractmethod
    def get_diem(self):
        pass  # phương thức trừu tượng, chưa có cách tính điểm

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngành: {self.nganh}")
        print(f"Điểm: {self.get_diem():.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")


# Lớp con cụ thể để kiểm thử lớp trừu tượng
class SinhVienTest(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem):
        super().__init__(ho_ten, nganh)
        self._diem = diem

    def get_diem(self):
        return self._diem
