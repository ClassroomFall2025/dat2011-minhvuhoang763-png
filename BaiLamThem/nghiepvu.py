from taikhoan import TaiKhoan
from importCSV import ghi_tai_khoan_vao_csv
from datetime import datetime

def tim_theo_so_tai_khoan(danh_sach, so_tai_khoan):
    for tk in danh_sach:
        if tk.so_tai_khoan == so_tai_khoan:
            return tk
    return None


def tao_tai_khoan_moi(danh_sach):
    so_tai_khoan = input("Nhập số tài khoản: ")
    if tim_theo_so_tai_khoan(danh_sach, so_tai_khoan):
        print("Số tài khoản đã tồn tại!")
        return

    ten = input("Nhập tên chủ tài khoản: ")
    loai = input("Loại tài khoản (T - Tiết kiệm / C - Cá nhân): ").upper()
    so_du = float(input("Nhập số dư ban đầu: "))

    if loai == 'T' and so_du < 500000:
        print("Tài khoản tiết kiệm yêu cầu số dư tối thiểu 500.000 VND!")
        return
    elif loai == 'C' and so_du < 1000000:
        print("Tài khoản cá nhân yêu cầu số dư tối thiểu 1.000.000 VND!")
        return

    tk = TaiKhoan(so_tai_khoan, ten, loai, so_du)
    danh_sach.append(tk)
    ghi_tai_khoan_vao_csv(danh_sach)
    print("Tạo tài khoản thành công!")


def hien_thi_danh_sach(danh_sach):
    print("\n=== DANH SÁCH TÀI KHOẢN ===")
    for tk in danh_sach:
        tk.hien_thi_tai_khoan()


def xoa_tai_khoan(danh_sach):
    so_tk = input("Nhập số tài khoản cần xóa: ")
    tk = tim_theo_so_tai_khoan(danh_sach, so_tk)
    if tk:
        danh_sach.remove(tk)
        ghi_tai_khoan_vao_csv(danh_sach)
        print("Đã xóa tài khoản thành công!")
    else:
        print("Không tìm thấy tài khoản!")


def chinh_sua_tai_khoan(danh_sach):
    so_tk = input("Nhập số tài khoản cần chỉnh sửa: ")
    tk = tim_theo_so_tai_khoan(danh_sach, so_tk)
    if not tk:
        print("Không tìm thấy tài khoản!")
        return

    tk.ten = input(f"Tên mới ({tk.ten}): ") or tk.ten
    tk.loai = input(f"Loại mới (T/C) ({tk.loai}): ").upper() or tk.loai
    try:
        so_du_moi = input(f"Số dư mới ({tk.so_du}): ")
        if so_du_moi:
            tk.so_du = float(so_du_moi)
    except ValueError:
        print("Số dư nhập không hợp lệ!")

    ghi_tai_khoan_vao_csv(danh_sach)
    print("Cập nhật thông tin thành công!")


def tim_kiem_theo_ten(danh_sach):
    tu_khoa = input("Nhập tên hoặc từ khóa cần tìm: ").lower()
    ket_qua = [tk for tk in danh_sach if tu_khoa in tk.ten.lower()]
    if not ket_qua:
        print("Không tìm thấy tài khoản nào!")
    else:
        print("=== KẾT QUẢ TÌM KIẾM ===")
        for tk in ket_qua:
            tk.hien_thi_tai_khoan()


def xuat_bao_cao(danh_sach):
    tong_tk = len(danh_sach)
    tong_so_du = sum(tk.so_du for tk in danh_sach)
    tiet_kiem = len([tk for tk in danh_sach if tk.loai == 'T'])
    ca_nhan = len([tk for tk in danh_sach if tk.loai == 'C'])

    noi_dung = (
        f"===== BÁO CÁO NGÂN HÀNG =====\n"
        f"Tổng số tài khoản: {tong_tk}\n"
        f"Tổng số dư: {tong_so_du:,.0f} VND\n"
        f"Tài khoản tiết kiệm: {tiet_kiem}\n"
        f"Tài khoản cá nhân: {ca_nhan}\n"
    )

    ten_file = f"baocao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
    print(f"Báo cáo đã được ghi vào file {ten_file}")
