import os
import telebot
import requests
import datetime
import time

API_KEY = os.environ['api_key']
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.send_message(message.chat.id, "Hey! I am the zodiac bot..")
    bot.send_message(message.chat.id, "Send me your zodiac sign and I'll tell you your horoscope!")

@bot.message_handler(commands=['zodiacs', 'Zodiacs'])
def poll_sender(message):
    bot.send_poll(message.chat.id, question='choose one!', options=['a', 'b', 'c', 'd'], type='quiz', correct_option_id=1, is_anonymous=False)

@bot.poll_answer_handler()
def handle_poll_answer(pollAnswer):
  print(pollAnswer)


@bot.message_handler(func=lambda m: True)
def identify_signs(message):
    time.sleep(1)
    bot.send_message(message.chat.id, "Hmm.. let me see.....")
    if message.text.lower() in [
            'aquarius', 'scorpio', 'virgo', 'aries', 'leo', 'gemini', 'cancer',
            'libra', 'sagittarius', 'capricorn', 'pisces', 'taurus']:
        sign = message.text.lower()
        url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
        headers = {
            'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
            'x-rapidapi-key':
            "582dbb69d4mshb9f9d4742ad7993p1702d9jsn2a5a5999c7db"
        }
        querystring = {"sign":sign,"day":"today"}
        day = datetime.datetime.now()
        day = day.strftime("%A")
        response = requests.request("POST", url, headers=headers, params=querystring)
        response_dict = eval(response.text)
        time.sleep(2)
        bot.send_message(message.chat.id, response_dict['description'])
        bot.send_message(message.chat.id, f"your mood today might be a bit {response_dict['mood']}")
        bot.send_message(message.chat.id, f"your luckly color for today is {response_dict['color']}")
        bot.send_message(message.chat.id, f"your luckly number for today is {response_dict['lucky_number']}")
    else:
      bot.reply_to(message, "This is not a valid zodiac sign you dumb bitch")




bot.infinity_polling()
