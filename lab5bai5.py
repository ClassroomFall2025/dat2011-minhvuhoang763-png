# ...existing code...
import math
import time

class MayTinhKhoaHoc:
    def __init__(self):
        self.lich_su = []

    def cong(self, so1, so2):
        kq = so1 + so2
        self.lich_su.append(f"{so1} + {so2} = {kq}")
        return kq

    def tru(self, so1, so2):
        kq = so1 - so2
        self.lich_su.append(f"{so1} - {so2} = {kq}")
        return kq

    def nhan(self, so1, so2):
        kq = so1 * so2
        self.lich_su.append(f"{so1} * {so2} = {kq}")
        return kq

    def chia(self, so1, so2):
        if b == 0:
            self.lich_su.append(f"{so1} / {so2} = Lỗi chia cho 0")
            return "Lỗi: Không chia được cho 0"
        kq = so1 / so2
        self.lich_su.append(f"{so1} / {so2} = {kq}")
        return kq

    def luy_thua(self, co_so, so_mu):
        kq = co_so ** so_mu
        self.lich_su.append(f"{co_so}^{so_mu} = {kq}")
        return kq

    def can_bac_2(self, so):
        if so < 0:
            self.lich_su.append(f"√{so} = Lỗi số âm")
            return "Lỗi: Không tính căn bậc hai số âm"
        kq = math.sqrt(so)
        self.lich_su.append(f"√{so} = {kq}")
        return kq

    def ham_luong_giac(self, goc):
        rad = math.radians(goc)
        sin_val = math.sin(rad)
        cos_val = math.cos(rad)
        tan_val = math.tan(rad)
        cot_val = 1 / tan_val if abs(tan_val) > 1e-12 else "Không xác định"
        self.lich_su.append(f"sin({goc})={sin_val}, cos({goc})={cos_val}, tan({goc})={tan_val}, cot({goc})={cot_val}")
        return sin_val, cos_val, tan_val, cot_val

    def logarit(self, doi_so, co_so=10):
        if doi_so <= 0:
            self.lich_su.append(f"log_{co_so}({doi_so}) = Lỗi")
            return "Lỗi: log chỉ nhận số dương"
        if co_so == 'e' or co_so == math.e:
            kq = math.log(doi_so)
            self.lich_su.append(f"ln({doi_so}) = {kq}")
        else:
            kq = math.log(doi_so, co_so)
            self.lich_su.append(f"log_{co_so}({doi_so}) = {kq}")
        return kq

    def giai_pt_bac_nhat(self, a, b):
        if a == 0:
            self.lich_su.append(f"{a}x + {b} = 0: Vô nghiệm hoặc vô số nghiệm")
            return "Phương trình vô nghiệm hoặc vô số nghiệm"
        x = -b / a
        self.lich_su.append(f"{a}x + {b} = 0 => x = {x}")
        return x

    def giai_pt_bac_hai(self, a, b, c):
        if a == 0:
            return self.giai_pt_bac_nhat(b, c)
        delta = b**2 - 4*a*c
        if delta < 0:
            self.lich_su.append(f"{a}x^2 + {b}x + {c} = 0: Vô nghiệm")
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            self.lich_su.append(f"{a}x^2 + {b}x + {c} = 0: Nghiệm kép x = {x}")
            return x
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            self.lich_su.append(f"{a}x^2 + {b}x + {c} = 0: x1 = {x1}, x2 = {x2}")
            return x1, x2

    def xem_lich_su(self):
        return list(self.lich_su)

    def hien_thi_thoi_gian(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")
# ...existing code...