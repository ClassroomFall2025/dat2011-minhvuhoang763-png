# filepath: e:\Python\dat2011-minhvuhoang763-png\assignment1.py
# Yêu cầu của asm
# Y1. Nhập danh sách nhân viên từ bàn phím, lưu thông tin vào file
# Y2. Đọc thông tin nhân viên từ file và xuất thông tin nhân viên ra màn hình.
# Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím
# Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật vào file data
# Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím. Cập nhật vào file data
# Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.
# Y7. Sắp xếp nhân viên theo họ và tên
# Y8. Xắp xếp nhân viên theo thu nhập
# Y9. Xuất 5 nhân viên có thu nhập cao nhất
def NhapNhanVien():
    print("Chức năng Y1: Nhập danh sách nhân viên từ bàn phím và lưu vào file")

def DocNhanVien():
    print("Chức năng Y2: Đọc thông tin nhân viên từ file và xuất danh sách")

def TimTheoMa():
    print("Chức năng Y3: Tìm và hiển thị nhân viên theo mã")

def XoaNhanVien():
    print("Chức năng Y4: Xóa nhân viên theo mã và cập nhật file")

def CapNhatNhanVien():
    print("Chức năng Y5: Cập nhật thông tin nhân viên theo mã và ghi file")

def TimTheoLuong():
    print("Chức năng Y6: Tìm các nhân viên theo khoảng lương")

def SapXepTen():
    print("Chức năng Y7: Sắp xếp nhân viên theo họ tên")

def SapXepThuNhap():
    print("Chức năng Y8: Sắp xếp nhân viên theo thu nhập")

def Top5ThuNhap():
    print("Chức năng Y9: Xuất 5 nhân viên có thu nhập cao nhất")


def menu():
    while True:
        print("\n===== MENU QUẢN LÝ NHÂN VIÊN =====")
        print("1. Nhập danh sách nhân viên")
        print("2. Đọc danh sách nhân viên từ file")
        print("3. Tìm nhân viên theo mã")
        print("4. Xóa nhân viên theo mã")
        print("5. Cập nhật nhân viên theo mã")
        print("6. Tìm nhân viên theo khoảng lương")
        print("7. Sắp xếp nhân viên theo họ tên")
        print("8. Sắp xếp nhân viên theo thu nhập")
        print("9. Xuất 5 nhân viên có thu nhập cao nhất")
        print("0. Thoát")
        
        try:
            chon = int(input("Chọn chức năng: "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
            continue
        
        match chon:
            case 1: NhapNhanVien()
            case 2: DocNhanVien()
            case 3: TimTheoMa()
            case 4: XoaNhanVien()
            case 5: CapNhatNhanVien()
            case 6: TimTheoLuong()
            case 7: SapXepTen()
            case 8: SapXepThuNhap()
            case 9: Top5ThuNhap()
            case 0:
                print("Thoát chương trình.")
                break
            case _: print("Chọn sai, vui lòng nhập lại.")

if __name__ == "__main__":
    menu()
