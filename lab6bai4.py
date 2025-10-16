from abc import ABC, abstractmethod

class SinhVienPoly(ABC):
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh

    @abstractmethod
    def get_diem(self):
        pass

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


class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, java, html, css):
        super().__init__(ho_ten, "IT")
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, marketing, sales):
        super().__init__(ho_ten, "Biz")
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3
