# bai1_module.py

def tach_ho_ten(ho_ten: str):
    """Tách họ, tên đệm, tên từ chuỗi họ tên đầy đủ."""
    danh_sach_tu = ho_ten.strip().split()
    if len(danh_sach_tu) == 0:
        return {"ho": "", "ten_dem": "", "ten": ""}
    ho = danh_sach_tu[0].upper()
    ten = danh_sach_tu[-1].upper()
    ten_dem = " ".join(danh_sach_tu[1:-1]) if len(danh_sach_tu) > 2 else ""
    return {"ho": ho, "ten_dem": ten_dem, "ten": ten}
