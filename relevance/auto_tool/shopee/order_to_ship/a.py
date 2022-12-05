# import
from selenium import webdriver
from time import sleep
import csv
import traceback
from consts import *
from utils import *
from get_product_utils import *
from datetime import datetime, timedelta
import re

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
# options.add_argument('headless')

# link = r'https://banhang.shopee.vn/portal/sale/order?type=unpaid'
link = r'https://banhang.shopee.vn/portal/sale/shipment?type=toship'
# link = r'https://banhang.shopee.vn/portal/sale/order?type=shipping'
# link = r'https://banhang.shopee.vn/portal/sale/shipment?type=toship&source=to_process'
login_link = r'https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F'
browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
browser.maximize_window()

data = []
detail_links = []
dict_total_products = {}
tong_doanh_thu = 0
tong_gia_nhap = 0

# login
browser.get(login_link)
waitElement('//button[text()="Đăng nhập"]', browser, 10)
sleep(1)
browser.find_element_by_class_name('_7nvtMo').click()
sleep(15)

# start
browser.get(link)
sleep(1)
# pass through intro
waitElement('//span[contains(text(), "Tiếp theo")]', browser, 10)
sleep(2)
browser.find_element_by_xpath('//span[contains(text(), "Tiếp theo")]').find_element_by_xpath('..').click()
sleep(1)
browser.find_elements_by_xpath('//span[contains(text(), "Tiếp theo")]')[-1].find_element_by_xpath('..').click()
sleep(1)
browser.find_element_by_xpath('//span[contains(text(), "Xác nhận")]').find_element_by_xpath('..').click()
sleep(1)

def getLinks():
    order_item_list = browser.find_elements_by_xpath('//a[@class="order-item"]')[:]
    for order_item in order_item_list:
        order_link = order_item.get_attribute('href')
        detail_links.append(order_link)
    sleep(2)

waitElement('//a[@class="order-item"]', browser)
getLinks()

# check if multiple page
try: # multiple pages
    number_of_pages = browser.find_elements_by_class_name('shopee-pager__page')[-1].text
    for i in range(2, int(number_of_pages) + 1):
        browser.find_element_by_xpath(f'//li[@class="shopee-pager__page"][text()={i}]').click()
        # get more link
        waitElement('//a[@class="order-item"]', browser)
        getLinks()
except Exception as e: # one page
    # traceback.print_exc()
    pass

writeToFile(log_file, getTime() + f' {len(detail_links)} orders!')
writeToFile('log.txt', '' ,mode='w')

# go to detail
for detail_link in detail_links:
    try:
        browser.get(detail_link)
        waitElement('//*[@class="qty"]', browser, 10)
        browser.find_element_by_class_name('toggle').click()
        sleep(1)
        log_info_header = browser.find_element_by_class_name('log-info-header')
        ma_van_don = ''
        dvvc = ''
        try:
            ma_van_don = log_info_header.find_element_by_class_name('label').text.split(' ')[-1]
            dvvc = log_info_header.find_element_by_class_name('actual-carrier-name').text
        except:
            pass
        luu_y = ''
        shop_note = ''
        try:
            luu_y = browser.find_element_by_xpath("//*[@class='description indent-more']").text
        except: pass
        try:
            shop_note = browser.find_element_by_xpath("//*[@class='note shopee-card']").get_attribute('content')
        except: pass
        dia_chi = browser.find_element_by_class_name('ship-address').find_element_by_xpath('..').text
        sdt = re.findall(r'\b\d{10,15}\b', dia_chi)[0]
        raw_shipping_fee = browser.find_elements_by_class_name('income-value')[1].text
        phi_van_chuyen = convertTextToNumber(raw_shipping_fee)
        raw_transaction_fee = browser.find_elements_by_class_name('income-value')[-2].text
        phi_giao_dich = convertTextToNumber(raw_transaction_fee)
        raw_revenue = browser.find_element_by_class_name('big-total').text
        doanh_thu = convertTextToNumber(raw_revenue) - phi_van_chuyen
        tong_doanh_thu += doanh_thu
        status_log = browser.find_elements_by_class_name('status-log')[-1]
        thoi_gian_dat_hang = status_log.find_element_by_class_name('time').text
        first_shopee_cart_content = browser.find_element_by_class_name('shopee-card__content')

        # tìm đơn có hạn giao trước ngày mai
        han_giao = ''
        try:
            browser.find_element_by_xpath('//div[contains(text(), "Giao hàng thành công")]')
        except:
            try:
                han_giao_raw = first_shopee_cart_content.find_element_by_class_name('body').text
                han_giao = han_giao_raw.rsplit(' ')[-1].strip('.') if 'nhất vào' in han_giao_raw else ''
                if han_giao and datetime.strptime(han_giao, '%d/%m/%Y') < datetime.now() + timedelta(1):
                    pass
                else:
                    han_giao = ''
            except:
                pass
        
        # lấy danh sách sản phẩm trong 1 đơn
        dict_products = {}
        product_list_element = browser.find_elements_by_class_name('product-list-item')[1:]
        for product_element in product_list_element:
            raw_qty = int(product_element.find_element_by_class_name('qty').text.strip())
            raw_sku = product_element.find_element_by_class_name('product-meta').text.split(':')[-1].strip()
            if '+' in raw_sku:
                skus = raw_sku.split(' + ')
            else:
                skus = [raw_sku]
            for sku in skus:
                qty = raw_qty    
                if sku.split(' ', 1)[0].isdigit():
                    q, s = sku.split(' ', 1)
                    qty *= int(q)
                    sku = s.strip()
                dict_products[sku] = dict_products.get(sku, 0) + qty

        Buy10GiveKichRe(dict_products)
        
        san_pham = getStringProductFromDictProduct(dict_products, dict_total_products)

        writeToFile('log.txt', f'{sdt}, {ma_van_don}, {san_pham}')
    
        data.append({
            SDT: sdt,
            MA_VAN_DON: ma_van_don,
            DVVC: dict_dvvc[dvvc],
            SAN_PHAM: san_pham,
            LUU_Y: luu_y + shop_note,
            DOANH_THU: doanh_thu,
            TRU_VON: doanh_thu - sum(dict_products[sku] * dict_product_import_price[sku] for sku in dict_products.keys()),
            PHI_VAN_CHUYEN: phi_van_chuyen,
            PHI_GIAO_DICH: phi_giao_dich,
            THOI_GIAN_DAT_HANG: thoi_gian_dat_hang,
            QUA_HAN_GIAO: han_giao,
            LINK: detail_link,
            **dict_products,
        })
    except:
        traceback.print_exc()
        writeToFile(log_file, f'{getTime()} Lỗi: {detail_link}')
        print(f'{getTime()} Lỗi: {detail_link}')
data = data[::-1]

data.append({})

data.append({
    PHI_GIAO_DICH: "Tổng doanh thu",
    DOANH_THU: tong_doanh_thu,
    **dict_total_products,
})

data.append({sku: dict_product_import_price[sku] for sku in dict_total_products.keys()})

dict_import_prices = {}
for sku in dict_total_products.keys():
    dict_import_prices[sku] = dict_total_products[sku] * dict_product_import_price.get(sku, 0)
tong_gia_nhap = sum(dict_import_prices.values())
data.append({
    PHI_GIAO_DICH: "Tổng giá nhập",
    DOANH_THU: tong_gia_nhap,
    **dict_import_prices,
})

data.append({
    PHI_GIAO_DICH: "Tổng lợi nhuận",
    DOANH_THU: tong_doanh_thu - tong_gia_nhap,
})

sleep(1)
browser.close()

with open(data_file, 'w', newline='', encoding="utf-8") as csvfile:
    csvfile.write(u'\ufeff') # utf8 with BOM
    writer = csv.DictWriter(csvfile, fieldnames=[*before_fields, *dict_total_products.keys(), *after_fields])
    writer.writeheader()
    writer.writerows(data)

writeToFile(log_file, getTime() + " DONE!\n")
print('DONE !')

### code này giúp lấy thêm số điện thoại + địa chỉ cụ thể của từng khách hàng