class Hang:

    def _init_(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def _str_(self):
        return f"Mã hàng: {self.ma_hang}, Tên hàng: {self.ten_hang}, Nhà sx: {self.nha_sx}, Giá: {self.gia}"
    class HangDienMay(Hang):

        def _int_(self,ma_hang, ten_hang, nha_sx, gia, tgbh, dien_ap, cong_suat):
            super()._init_(ma_hang, ten_hang, nha_sx, gia)
            self.tgbh = tgbh
            self.dien_ap = dien_ap
            self.cong_suat = cong_suat

        def _str_(self):
            return super()._str_() + f"Thời gian bảo hành: {self.tgbh} Điện áp: {self.dien_ap}, Công suất: {self.cong_suat}"
        
class HangSanhSu(Hang):

    def __init__(self,ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hh):
        super()._init_(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hh = ngay_hh

    def _str_(self):
        return super()._str_() +f"Ngày sx: {self.ngay_sx}, Ngày hh: {self.ngay_hh}"
    
