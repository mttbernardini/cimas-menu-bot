#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Gianmaria Del Monte

import telepot, locale, menus, calendar
from datetime import datetime

TOKEN='633120718:AAGPAeiYo7xWwAdM9lGeG0GotmGlzJXQ8QQ'
CHANNEL_ID = -1001186126012

DEFAULT_MSG = "Il menu di oggi non è disponibile"

def get_today_menu():
	locale.setlocale(locale.LC_TIME, ("it_IT", "UTF-8"))
	now = datetime.now().date()
	
	try:
		menu = menus.getMenus()[now]
		msg = "🍴 Il menu di oggi (%s %d %s)\n" % (calendar.day_name[now.weekday()], now.day, calendar.month_name[now.month])
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
