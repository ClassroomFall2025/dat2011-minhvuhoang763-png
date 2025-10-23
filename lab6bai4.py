

class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.__ho_ten = ho_ten
        self.__nganh = nganh

    def get_diem(self):
        pass  # sẽ được ghi đè ở lớp con

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
        print(f"Họ tên: {self.__ho_ten}")
        print(f"Ngành: {self.__nganh}")
        print(f"Điểm: {self.get_diem():.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")


class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, java, html, css):
        super().__init__(ho_ten, "IT")
        self.__java = java
        self.__html = html
        self.__css = css

    def get_diem(self):
        return (2 * self.__java + self.__html + self.__css) / 4


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, marketing, sales):
        super().__init__(ho_ten, "Biz")
        self.__marketing = marketing
        self.__sales = sales

    def get_diem(self):
        return (2 * self.__marketing + self.__sales) / 3
