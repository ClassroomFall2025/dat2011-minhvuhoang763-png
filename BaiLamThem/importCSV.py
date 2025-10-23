import csv
import os
import shutil
from datetime import datetime
from taikhoan import TaiKhoan

def doc_tai_khoan_tu_csv(ten_file='taikhoan.csv'):
    danh_sach = []
    if os.path.exists(ten_file):
        with open(ten_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tk = TaiKhoan(row['soTaiKhoan'], row['ten'], row['loai'], float(row['soDu']))
                danh_sach.append(tk)
    return danh_sach


def ghi_tai_khoan_vao_csv(danh_sach, ten_file='taikhoan.csv'):
    with open(ten_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['soTaiKhoan', 'ten', 'loai', 'soDu']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tk in danh_sach:
            writer.writerow(tk.to_dict())


def sao_luu_du_lieu():
    if not os.path.exists('backup'):
        os.mkdir('backup')
    ten_moi = f"backup/taikhoan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    shutil.copy('taikhoan.csv', ten_moi)
    print(f"Đã sao lưu dữ liệu sang {ten_moi}")


def khoi_phuc_du_lieu():
    if not os.path.exists('backup'):
        print("Chưa có thư mục backup!")
        return
    danh_sach_file = os.listdir('backup')
    for i, f in enumerate(danh_sach_file):
        print(f"{i+1}. {f}")
    try:
        chon = int(input("Chọn số file cần khôi phục: ")) - 1
        file_chon = os.path.join('backup', danh_sach_file[chon])
        shutil.copy(file_chon, 'taikhoan.csv')
        print(f"Đã khôi phục dữ liệu từ {file_chon}")
    except Exception:
        print("Lựa chọn không hợp lệ!")
