from dotenv import dotenv_values

config = dotenv_values(".env")
username = config["username"]
password = config["password"]

MA_VAN_DON = 'Mã vận đơn'
DVVC = 'ĐVVC'
DIA_CHI = 'Địa chỉ'
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
    DVVC,
    LUU_Y,
    THOI_GIAN_DAT_HANG,
    QUA_HAN_GIAO,
    PHI_VAN_CHUYEN,
    PHI_GIAO_DICH,
    DOANH_THU,
    TRU_VON,
]
after_fields = [
    LINK,
    DIA_CHI,
]

dict_dvvc = {
    'Giao Hàng Nhanh': 'GHN',
    'Giao Hàng Tiết Kiệm': 'GHTK',
    'J&T Express': 'J&T',
    '': '',
    'Lỗi. Không thể hiển thị đơn vị vận chuyển.': 'Error',
}

dict_product_import_price = {
    'leo': 6000,
    'hồng 13': 6000,
    'hồng 12': 6000,
    'hồng 15k': 6000,
    'cành chiết gỗ': 10000,
    'cành chiết leo': 10000,
    'kích rễ': 3000,
    'hồng 8k': 3500,
    'hồng': 3500,
    'huệ 13k': 2000,
    'huệ 9k': 1500,
    'huệ to': 2000,
    'huệ nhỏ': 1500,
    'huệ 7k': 2000,
    'huệ 5k': 1500,
    'Lời tri ân': 0,
    'cóc thái': 18000,
    'cau lùn': 16000,
    'gang tay hươu': 6000,
    'hạt giống cải bẹ': 8000,
    'trà my 1 tán 40cm 30k': 30000,
    'đỗ quyên 79k': 50000,
    'giá thể vỏ thông': 5000,
    'dây tây 30': 15000,
    'đồng tiền kép': 2000,
    'gốc tỷ muội': 8000,
    'hồng 20': 8000,
    'hồng kít': 8000,
}

data_file = 'data_order_to_ship.csv'
log_file = 'log_order_to_ship.txt'