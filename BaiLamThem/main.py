from importCSV import *
from nghiepvu import *

def menu():
    danh_sach = doc_tai_khoan_tu_csv()

    while True:
        print("""
======== HỆ THỐNG QUẢN LÝ NGÂN HÀNG ========
1. Tạo tài khoản mới
2. Gửi tiền
3. Rút tiền
4. Kiểm tra số dư
5. Danh sách tất cả tài khoản
6. Xóa tài khoản
7. Chỉnh sửa tài khoản
8. Tìm kiếm theo tên
9. Xuất báo cáo
10. Sao lưu dữ liệu
11. Khôi phục dữ liệu
12. Thoát
============================================
""")
        try:
            chon = int(input("Chọn chức năng: "))
        except ValueError:
            print("Vui lòng nhập số từ 1–12!")
            continue

        if chon == 1:
            tao_tai_khoan_moi(danh_sach)
        elif chon == 2:
            so_tk = input("Nhập số tài khoản: ")
            tk = tim_theo_so_tai_khoan(danh_sach, so_tk)
            if tk:
                so_tien = float(input("Nhập số tiền cần gửi: "))
                tk.gui_tien(so_tien)
                ghi_tai_khoan_vao_csv(danh_sach)
            else:
                print("Không tìm thấy tài khoản!")
        elif chon == 3:
            so_tk = input("Nhập số tài khoản: ")
            tk = tim_theo_so_tai_khoan(danh_sach, so_tk)
            if tk:
                so_tien = float(input("Nhập số tiền cần rút: "))
                tk.rut_tien(so_tien)
                ghi_tai_khoan_vao_csv(danh_sach)
            else:
                print("Không tìm thấy tài khoản!")
        elif chon == 4:
            so_tk = input("Nhập số tài khoản: ")
            tk = tim_theo_so_tai_khoan(danh_sach, so_tk)
            if tk:
                tk.hien_thi_tai_khoan()
            else:
                print("Không tìm thấy tài khoản!")
        elif chon == 5:
            hien_thi_danh_sach(danh_sach)
        elif chon == 6:
            xoa_tai_khoan(danh_sach)
        elif chon == 7:
            chinh_sua_tai_khoan(danh_sach)
        elif chon == 8:
            tim_kiem_theo_ten(danh_sach)
        elif chon == 9:
            xuat_bao_cao(danh_sach)
        elif chon == 10:
            sao_luu_du_lieu()
        elif chon == 11:
            khoi_phuc_du_lieu()
            danh_sach = doc_tai_khoan_tu_csv()  # đọc lại sau khôi phục
        elif chon == 12:
            print("Tạm biệt! Cảm ơn bạn đã sử dụng hệ thống.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
