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

@bot.message_handler(func=lambda message: True)
def get_my_id(message):
    # Con bot sẽ rep lại chính xác ID tài khoản Telegram của bạn
    print(f"Chat ID của bạn là: {message.chat.id}")
    bot.reply_to(message, f"🎯 CHAT_ID của bạn là: `{message.chat.id}`", parse_mode="Markdown")
    
# Chạy bot liên tục (Long Polling)
bot.infinity_polling()
