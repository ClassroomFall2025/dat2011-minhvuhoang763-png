class SanPham:
    """
    Lớp SanPham:
    - Có 3 thuộc tính: ten, gia, giam_gia
    - Có hàm khởi tạo truyền 3 tham số
    - Có các phương thức: tinh_thue(), xuat(), nhap()
    """

    def __init__(self, ten, gia, giamgia):
        self.ten = ten
        self.gia = gia
        self.giamgia = giamgia

    def tinh_thue(self):
        """Tính thuế nhập khẩu = 10% giá sản phẩm"""
        return self.gia * 0.10

    def xuat(self):
        """In thông tin sản phẩm ra màn hình"""
        print(f"Sản phẩm {self.ten} có giá {self.gia} được giảm giá {self.giamgia} và phải đóng thuế {self.tinh_thue()}")

    def nhap(self):
        """Nhập thông tin sản phẩm từ bàn phím"""
        self.ten = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập đơn giá: "))
        self.giamgia = float(input("Nhập giảm giá: "))
