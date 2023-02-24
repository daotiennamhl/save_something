from dotenv import dotenv_values

config = dotenv_values(".env")
username = config["username"]
password = config["password"]

MA_VAN_DON = 'Mã vận đơn'
DVVC = 'ĐVVC'
SDT = 'Sđt'
SAN_PHAM = 'Sản phẩm'
LUU_Y = 'Lưu ý'
DOANH_THU = 'Doanh Thu'
PHI_VAN_CHUYEN = 'Phí vận chuyển'
PHI_GIAO_DICH = 'Phí giao dịch'
THOI_GIAN_DAT_HANG = 'Thời gian đặt hàng'
QUA_HAN_GIAO = 'Quá hạn giao'
LINK = 'Link'
TRU_VON = 'Trừ vốn'

before_fields = [
    MA_VAN_DON,
    SAN_PHAM,
    THOI_GIAN_DAT_HANG,
    SDT,
    DVVC,
    LUU_Y,
    QUA_HAN_GIAO,
    PHI_VAN_CHUYEN,
    PHI_GIAO_DICH,
    DOANH_THU,
    TRU_VON,
]
after_fields = [
    LINK,
]

dict_dvvc = {
    'Giao Hàng Nhanh': 'GHN',
    'Giao Hàng Tiết Kiệm': 'GHTK',
    'J&T Express': 'J&T',
    'Shopee Xpress': 'SPX',
    '': '',
    'Lỗi. Không thể hiển thị đơn vị vận chuyển.': 'Error',
}

data_file = 'data_order_to_ship.csv'
log_file = 'log_order_to_ship.txt'