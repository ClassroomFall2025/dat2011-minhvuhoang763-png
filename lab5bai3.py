class SanPham:
    def __init__(self, ten="", gia=0.0, giamgia=0.0):
        self.ten = ten
        self.gia = gia
        self.giamgia = giamgia

    # Getter và Setter cho từng thuộc tính
    def get_ten(self):
        return self.ten
    def set_ten(self, ten):
        self.ten = ten

    def get_gia(self):
        return self.gia
    def set_gia(self, gia):
        self.gia = gia

    def get_giam_gia(self):
        return self.giamgia
    def set_giam_gia(self, giamgia):
        self.giamgia = giamgia

    def tinh_thue(self):
        return self.gia * 0.10

    def xuat(self):
        print(f"Sản phẩm {self.ten} có giá {self.gia} được giảm giá {self.giamgia} và phải đóng thuế {self.tinh_thue()}")