# sanpham.py

# sanpham.py
class SanPham:
    """Lớp SanPham: gồm tên, giá, giảm giá và các phương thức xử lý."""
    
    def __init__(self, ten, gia, giamgia):
        self.ten = ten
        self.gia = gia
        self.giamgia = giamgia

    def tinh_thue(self):
        """Tính thuế nhập khẩu 10% giá sản phẩm"""
        return self.gia * 0.10

    def xuat(self):
        """Xuất thông tin sản phẩm"""
        print(f"Sản phẩm {self.ten} có giá {self.gia} được giảm giá {self.giamgia} và phải đóng thuế {self.tinh_thue()}")

