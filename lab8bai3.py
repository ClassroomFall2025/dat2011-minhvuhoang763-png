import random

def tao_file_so_ngau_nhien(ten_file="bai3_so_ngau_nhien.txt", so_luong=1_000_000, tu=0, den=100):
    """Sinh ngẫu nhiên các số và ghi ra file (mỗi số cách nhau bằng dấu cách)."""
    with open(ten_file, "w", encoding="utf-8") as tep:
        for i in range(so_luong):
            so = str(random.randint(tu, den))
            if i > 0:
                tep.write(" ")
            tep.write(so)
