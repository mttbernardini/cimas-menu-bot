#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Gianmaria Del Monte

import telepot
import menus
from datetime import datetime

TOKEN='633120718:AAGPAeiYo7xWwAdM9lGeG0GotmGlzJXQ8QQ'
CHANNEL_ID = -1001186126012

DEFAULT_MSG = "Il menù di oggi non è disponibile"

weeks = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
months = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

def get_today_menu():
	now = datetime(2019, 3, 18).date()
	
	try:
		menu = menus.getMenus()[now]
		msg = "🍴 Il menu di oggi (%s %d %s)\n" % (weeks[now.weekday()], now.day, months[now.month-1])
		msg += "-------------------------------------\n"
		
		for p in menu:
			msg += "*%s:*\n" % p
			for pasto in menu[p]:
				msg += " - %s\n" % pasto
			
		msg += "-------------------------------------\n"
		msg += "🍞 _Il pane è compreso nel pasto._\n"
		msg += "🥤 _Le bevande sono disponibili nei distributori all'interno della sala e sono libere._\n"
		msg += "🍊 _In alternativa alla frutta: yogurt, succhi di frutta o dessert._\n"
		return msg
		
	except:
		return DEFAULT_MSG

def send_msg(msg):
	bot = telepot.Bot(TOKEN)
	bot.sendMessage(CHANNEL_ID, msg, parse_mode= 'Markdown')

if __name__ == '__main__':
	send_msg(get_today_menu())
