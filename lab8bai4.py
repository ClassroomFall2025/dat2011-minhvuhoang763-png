import statistics

def thong_ke_tu_file(ten_file="bai3_so_ngau_nhien.txt"):
    """Tính trung bình (mean) và độ lệch chuẩn (stdev) từ file dữ liệu."""
    with open(ten_file, "r", encoding="utf-8") as tep:
        du_lieu = tep.read().strip()

    danh_sach_so = list(map(int, du_lieu.split()))
    trung_binh = statistics.mean(danh_sach_so)
    do_lech_chuan = statistics.pstdev(danh_sach_so)
    return trung_binh, do_lech_chuan
