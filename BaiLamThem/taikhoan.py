class TaiKhoan:
    def __init__(self, so_tai_khoan, ten, loai, so_du):
        self.so_tai_khoan = so_tai_khoan
        self.ten = ten
        self.loai = loai.upper()  # 'T' - Tiết kiệm, 'C' - Cá nhân
        self.so_du = float(so_du)

    def hien_thi_tai_khoan(self):
        print(f"Số TK: {self.so_tai_khoan} | Tên: {self.ten} | Loại: {self.loai} | Số dư: {self.so_du:,.0f} VND")

    def gui_tien(self, so_tien):
        if so_tien <= 0:
            print("Số tiền phải lớn hơn 0!")
            return
        self.so_du += so_tien
        print(f"Đã gửi {so_tien:,.0f} VND. Số dư mới: {self.so_du:,.0f} VND")

    def rut_tien(self, so_tien):
        if so_tien <= 0:
            print("Số tiền phải lớn hơn 0!")
            return
        if so_tien > self.so_du:
            print("Số dư không đủ để rút!")
            return
        self.so_du -= so_tien
        print(f"Đã rút {so_tien:,.0f} VND. Số dư còn lại: {self.so_du:,.0f} VND")

    def to_dict(self):
        return {
            'soTaiKhoan': self.so_tai_khoan,
            'ten': self.ten,
            'loai': self.loai,
            'soDu': self.so_du
        }

