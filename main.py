import os
import telebot
import time
from utils import call_zodiac_api

API_KEY = os.environ['api_key']
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.send_message(message.chat.id, "Hey! I am the zodiac bot..")
    bot.send_message(message.chat.id, "Send me your zodiac sign and I'll tell you your horoscope!")


@bot.message_handler(func=lambda m: True)
def identify_signs(message):
    time.sleep(1)
    bot.send_message(message.chat.id, "Hmm.. let me see.....")
    if message.text.lower() in [
            'aquarius', 'scorpio', 'virgo', 'aries', 'leo', 'gemini', 'cancer',
            'libra', 'sagittarius', 'capricorn', 'pisces', 'taurus']:
        sign = message.text.lower()
        response = call_zodiac_api(sign)
        response_dict = eval(response.text)
        time.sleep(2)
        bot.send_message(message.chat.id, response_dict['description'])
        bot.send_message(message.chat.id, f"your mood today might be a bit {response_dict['mood']}")
        bot.send_message(message.chat.id, f"your luckly color for today is {response_dict['color']}")
        bot.send_message(message.chat.id, f"your luckly number for today is {response_dict['lucky_number']}")
    else:
      bot.reply_to(message, "This is not a valid zodiac sign you dumb bitch")



while True:
  try:
    bot.infinity_polling()
  except:
    pass
