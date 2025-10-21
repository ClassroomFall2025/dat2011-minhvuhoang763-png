import re

mau_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$')
mau_dien_thoai = re.compile(r'^0\d{9,10}$')
mau_cmnd = re.compile(r'^\d{9}(\d{3})?$')

def kiem_tra_sinh_vien(thong_tin: dict):
    """Kiểm tra định dạng email, điện thoại, và CMND/CCCD."""
    loi = {}
    if not mau_email.match(thong_tin.get("email", "").strip()):
        loi["email"] = "Email không đúng định dạng"
    if not mau_dien_thoai.match(thong_tin.get("dien_thoai", "").strip()):
        loi["dien_thoai"] = "Số điện thoại phải có 10-11 chữ số và bắt đầu bằng 0"
    if not mau_cmnd.match(thong_tin.get("cmnd", "").strip()):
        loi["cmnd"] = "CMND/CCCD phải có 9 hoặc 12 chữ số"
    return loi
