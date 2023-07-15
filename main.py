import telebot

API_TOKEN = '6132467676:AAGLz2ZwszFTk9Iy3FBDRMAIblXwfg-YUcY'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, я ЭхоБот!
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    print(message.text)
    print(message)
bot.infinity_polling()