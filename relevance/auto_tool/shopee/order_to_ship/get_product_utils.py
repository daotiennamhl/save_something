dict_product_import_price = {
    'huệ mưa 4 củ': 1000,
    'huệ mưa 3 củ': 1000,
    'kích rễ': 3000,
    'Lời tri ân': 0,
    'cóc thái': 18000,
    'cau lùn': 16000,
    'củ ly': 5000,
    'gang tay hươu': 6000,
    'hạt giống cải bẹ': 8000,
    'trà my 1 tán 40cm 30k': 30000,
    'trà my nhiều tán 60cm': 130000,
    'trà my nhiều tán 70cm': 140000,
    'đỗ quyên 79k': 50000,
    'giá thể vỏ thông': 5000,
    'dây tây 30': 15000,
    'đồng tiền kép': 2000,
    'sứ thái kép 209k': 150000,
    'huệ đơn to': 4000,
    'huệ đơn nhỏ': 2000,
    'huệ kép to': 120000,
    'huệ kép nhỏ': 80000,
    'huệ kép': 100000,
    'cau 35cm': 20000,
    'cau 25cm': 15000,
    'gốc tỷ muội': 6000,
    'gốc ghép mắt': 5000,
    'hồng mới': 6000,
    'hồng đại': 3000,
    'hồng': 3000,
    'leo': 6000,
    'hồng cổ': 5000,
}

giveKichRe = ['gốc tỷ muội', 'gốc ghép mắt', 'hồng mới', 'hồng đại', 'hồng', 'leo']

kich_re = 'kích rễ'

def getStringProductFromDictProduct(dict_products, dict_total_products):
    san_pham = []
    for item in dict_products.items():
        p_sku, p_qty = item
        san_pham.append(f'{p_qty} {p_sku}')
        dict_products[p_sku] = p_qty
        dict_total_products[p_sku] = dict_total_products.get(p_sku, 0) + p_qty
    san_pham = ' + '.join(san_pham)
    return san_pham

def Buy10GiveKichRe(dict_products):
    dict_products[kich_re] = dict_products.get(kich_re, 0)
    for item in dict_products.items():
        p_sku, p_qty = item
        if p_sku in giveKichRe and p_qty >= 10:
            dict_products[kich_re] = dict_products.get(kich_re, 0) + int(p_qty/10)
    if dict_products[kich_re] == 0:
        del dict_products[kich_re]