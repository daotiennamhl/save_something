import re
import telebot
import requests

# 🔴 ĐIỀN THÔNG TIN CỦA BẠN VÀO ĐÂY
TELEGRAM_TOKEN = "8817552438:AAHYbCsXx3tNAGMjbjbz_CwRWyyYlixd35U"
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbxMD_s3GNrMpVHjTh9aekj5OchjbfVIsmaLpvcqWlcWNr5-11D6lO7Pkrll6bG_IkGHfQ/exec"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

print("Bot đang chạy...")

# Hàm xử lý chuẩn hóa số tiền (ví dụ: 50k -> 50000)
def parse_amount(amount_str):
    amount_str = amount_str.lower().strip()
    if 'k' in amount_str:
        amount_str = amount_str.replace('k', '')
        return int(float(amount_str) * 1000)
    return int(amount_str)

# Bắt sự kiện khi người dùng gõ tin nhắn text
@bot.message_handler(func=lambda message: True)
def handle_finance(message):
    text = message.text.strip()
    
    # Sử dụng Regex để tách phần Chữ (Khoản chi) và phần Số (Số tiền)
    # Hỗ trợ định dạng: "Tên_khoản_chi Số_tiền" (Ví dụ: Ăn trưa 50k hoặc Cafe 30000)
    match = re.match(r"^(.+)\s+(\d+(?:\.\d+)?k?|\d+)$", text, re.IGNORECASE)
    
    if match:
        item = match.group(1).strip()
        amount_raw = match.group(2).strip()
        
        try:
            amount = parse_amount(amount_raw)
            
            # Gửi dữ liệu sang Google Sheets thông qua Apps Script URL
            payload = {"item": item, "amount": amount}
            response = requests.post(GOOGLE_SHEET_URL, json=payload)
            
            if response.status_code == 200:
                bot.reply_to(message, f"✅ Đã ghi nhận: *{item}* -> *{amount:,}đ* vào Google Sheets!", parse_mode="Markdown")
            else:
                bot.reply_to(message, "❌ Lỗi kết nối với Google Sheets.")
        except Exception as e:
            bot.reply_to(message, f"❌ Có lỗi xảy ra khi xử lý dữ liệu: {str(e)}")
    else:
        bot.reply_to(message, "⚠️ Sai cú pháp rồi bạn ơi!\nHãy nhập theo dạng: `Tên_khoản_chi Số_tiền` (Ví dụ: `Ăn trưa 50k` hoặc `Mua sách 120000`)")

# Chạy bot liên tục (Long Polling)
bot.infinity_polling()
