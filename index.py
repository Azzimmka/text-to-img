from telebot import TeleBot
import os
from dotenv import load_dotenv, find_dotenv
from PIL import Image, ImageDraw, ImageFont
import uuid
FONT_PATH = "DejaVuSansBold.ttf" 
FONT_SIZE = 12

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = TeleBot(token=TOKEN)

COORDS = {
    "bank": (235, 270),
    "account": (235, 286),
    "fullname": (235, 301),
    "currency": (235, 316),
    "amount": (215, 185),
}

userState = {}
userDara = {}

WAITING_FOR_CARD = 'waiting_for_card'
WAITING_FOR_PHONE = 'waiting_for_phone'



@bot.message_handler(commands=['start'])
def startMessage(message):
    chatId = message.chat.id

    bot.send_message(chatId,"Введите данные одним сообщением, каждый пункт с новой строки:\n"
        "1) Название банка\n"
        "2) Номер счета\n"
        "3) ФИО\n"
        "4) Валюта\n"
        "5) Сумма и валюта\n\n"
        "Пример:\n"
        "BANRESERVAS\n"
        "96007913156\n"
        "DELINE OVELIS SOTO\n"
        "DOP\n"
        "300 DOP")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chatID = message.chat.id
    lines = message.text.split("\n")
    lines = [l.strip() for l in lines if l.strip()]

    if len(lines) != 5:
        bot.send_message(message.chat.id, "Ошибка: нужно 5 строк. Попробуйте снова.")        
        return 
    bank, account, fullname, currency, amount = lines

    img = Image.open('template.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Рисуем текст
    draw.text(COORDS["bank"], bank, font=font, fill="white")
    draw.text(COORDS["account"], account, font=font, fill="white")
    draw.text(COORDS["fullname"], fullname, font=font, fill="white")
    draw.text(COORDS["currency"], currency, font=font, fill="white")
    draw.text(COORDS["amount"], amount, font=font, fill="white")

    output = f"result{uuid.uuid4()}.png"
    img.save(output)


    with open(output, "rb") as f:
        bot.send_photo(message.chat.id, f)
        bot.send_message(chatID, 'Без наёбов только 😉')
    os.remove(output)




bot.infinity_polling()


