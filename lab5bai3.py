class SanPham:
    def __init__(self, ten="", gia=0.0, giamgia=0.0):
        self.__ten = ten
        self.__gia = gia
        self.__giamgia = giamgia

    # Getter và Setter cho từng thuộc tính
    def get_ten(self):
        return self.__ten
    def set_ten(self, ten):
        self.__ten = ten

    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giamgia
    def set_giam_gia(self, giamgia):
        self.__giamgia = giamgia

    def tinh_thue(self):
        return self.__gia * 0.10

    def xuat(self):
        print(f"Sản phẩm {self.__ten} có giá {self.__gia} được giảm giá {self.__giamgia} và phải đóng thuế {self.tinh_thue():,.0f} VNĐ")
