# BÀI 1: TÍnh Tiền Nước

def TinhTienNuoc(SoNuoc):
    GiaBanNuoc = (7500, 8800, 12000, 24000)
    if SoNuoc <=10:
        TienNuoc = SoNuoc * GiaBanNuoc[0]
    elif SoNuoc >10 and SoNuoc <=20:
        TienNuoc = 10 * GiaBanNuoc[0] + (SoNuoc - 10 ) * GiaBanNuoc[1]
    elif SoNuoc >20 and SoNuoc <=30:
        TienNuoc = 10 * GiaBanNuoc[0] + 10 * GiaBanNuoc[1] + (SoNuoc - 20) * GiaBanNuoc[2]
    else:
        TienNuoc = 10 * GiaBanNuoc[0] + 10 * GiaBanNuoc[1] + 10 * GiaBanNuoc[2] + (SoNuoc - 30) * GiaBanNuoc[3]
    return TienNuoc




# BÀI 2: Tính nguyên liệu làm bánh

def TinhNguyenLieu(SLbdx, SLbtc, SLbd) :
    BanhDauXanh = {"Đường": 0.04,"Đậu": 0.07}
    BanhThapCam = {"Đường": 0.06, "Đậu": 0}
    BanhDeo = {"Đường": 0.05, "Đậu": 0.02}
    NguyenLieu = {}
    DuongHopBanh = SLbdx * BanhDauXanh["Đường"] + SLbtc * BanhThapCam["Đường"] + SLbd * BanhDeo["Đường"]
    DauHopBanh = SLbdx * BanhDauXanh["Đậu"] + SLbtc * BanhThapCam["Đậu"] + SLbd * BanhDeo["Đậu"]
    NguyenLieu["Đường"] = DuongHopBanh
    NguyenLieu["Đậu"] = DauHopBanh
    return NguyenLieu


# BÀI 5: 
import math
import time

LichSu = []

def Cong(So1, So2):
    kq = So1 + So2
    LichSu.append(f"{So1} + {So2} = {kq}")
    return kq

def Tru(So1, So2):
    kq = So1 - So2
    LichSu.append(f"{So1} - {So2} = {kq}")
    return kq

def Nhan(So1, So2):
    kq = So1 * So2
    LichSu.append(f"{So1} * {So2} = {kq}")
    return kq

def Chia(So1, So2):
    if So2 == 0:
        LichSu.append(f"{So1} / {So2} = Lỗi chia cho 0")
        return "Lỗi: Không chia được cho 0"
    kq = So1 / So2
    LichSu.append(f"{So1} / {So2} = {kq}")
    return kq

def LuyThua(CoSo, SoMu):
    kq = CoSo ** SoMu
    LichSu.append(f"{CoSo}^{SoMu} = {kq}")
    return kq

def CanBac2(So):
    if So < 0:
        LichSu.append(f"√{So} = Lỗi số âm")
        return "Lỗi: Không tính căn bậc hai số âm"
    kq = math.sqrt(So)
    LichSu.append(f"√{So} = {kq}")
    return kq

def HamLuongGiac(goc):
    ham = math.radians(goc)
    singoc = math.sin(ham)
    cosgoc = math.cos(ham)
    tangoc = math.tan(ham)
    cotgoc = None
    if tangoc !=0:
        cotgoc = 1/tangoc
    else:
        cotgoc = "Không xác định"
    LichSu.append(f"sin({goc})={singoc}, cos({goc})={cosgoc}, tan({goc})={tangoc}")
    return singoc, cosgoc, tangoc, cotgoc

def logarit(DoiSo, CoSo=10):
    if DoiSo <= 0:
        LichSu.append(f"log_{CoSo}({DoiSo}) = Lỗi")
        return "Lỗi: log chỉ nhận số dương"
    if  CoSo == 'e':
        kq = math.log(DoiSo)
        LichSu.append(f"ln({DoiSo}) = {kq}")
        return kq
    else:
        kq = math.log(DoiSo, CoSo)
        LichSu.append(f"log_{CoSo}({DoiSo}) = {kq}")
        return kq

def giai_pt_bac_nhat(a, b):
    if a == 0:
        LichSu.append(f"{a}x + {b} = 0: Vô nghiệm hoặc vô số nghiệm")
        return "Phương trình vô nghiệm hoặc vô số nghiệm"
    x = -b / a
    LichSu.append(f"{a}x + {b} = 0 => x = {x}")
    return x

def giai_pt_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    if delta < 0:
        LichSu.append(f"{a}x^2 + {b}x + {c} = 0: Vô nghiệm")
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        LichSu.append(f"{a}x^2 + {b}x + {c} = 0: Nghiệm kép x = {x}")
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        LichSu.append(f"{a}x^2 + {b}x + {c} = 0: x1 = {x1}, x2 = {x2}")
        return x1, x2

def xem_lich_su():
    return LichSu

def hien_thi_thoi_gian():
    return time.strftime("%Y-%m-%d %H:%M:%S")