import time
import schedule
import telebot
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot('5349094339:AAEqDPvN5-uZQccWB_hPShycclGffAfrwk8')

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64'}
r = requests.get('https://psycatgames.com/ru/magazine/quotes/short-positive-quotes/', headers= headers)
r.encoding = 'utf-8'


soup = BeautifulSoup(r.text, 'html.parser')

data = soup.find_all('li')
for i in range(len(data)):
	 data[i] = data[i].text


@bot.message_handler(commands=['start'])
def nejniy_romatic(message):
	bot.send_message(message.chat.id,"Привет! Я создан, чтобы заряжать тебя энергией каждый день. Дождись 12:00.")
	iterat = 0
	while True:
		bot.send_message(message.chat.id, data[iterat])
		iterat += 1
		time.sleep(86400‬)
		


bot.infinity_polling()
