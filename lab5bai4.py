class SanPham:
    """
    Lớp SanPham:
    - Có 3 thuộc tính private: __ten, __gia, __giamgia
    - Có hàm khởi tạo truyền 3 tham số
    - Có các phương thức: tinh_thue(), xuat(), nhap()
    """

    def __init__(self, ten, gia, giamgia):
        self.__ten = ten
        self.__gia = gia
        self.__giamgia = giamgia

    def tinh_thue(self):
        """Tính thuế nhập khẩu = 10% giá sản phẩm"""
        return self.__gia * 0.10

    def xuat(self):
        """In thông tin sản phẩm ra màn hình"""
        print(f"Sản phẩm {self.__ten} có giá {self.__gia} được giảm giá {self.__giamgia} và phải đóng thuế {self.tinh_thue():,.0f} VNĐ")

    def nhap(self):
        """Nhập thông tin sản phẩm từ bàn phím"""
        self.__ten = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập đơn giá: "))
        self.__giamgia = float(input("Nhập giảm giá: "))

