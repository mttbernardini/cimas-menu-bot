#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Matteo Bernardini
# Copyright (c) 2019 Gianmaria Del Monte

import telepot, requests, locale, lxml.html
from sys import argv
from datetime import datetime, date

locale.setlocale(locale.LC_TIME, ("it_IT", "UTF-8"))

MENU_URL = "http://www.cimasristorazione.com/menu-mense/universita-roma-3/"
CHANNEL_ID = -1001186126012


def get_menus():
	r = requests.get(MENU_URL)
	dom = lxml.html.fromstring(r.text)
	menus = {}
	for div in dom.cssselect(".page-menu-mense .day-menu"):
		day = datetime.strptime(div.find_class("date")[0].text, "%d %B %Y").date()
		day_menu = {}
		for (h5, ul) in zip(div.cssselect(".tab-content h5"), div.cssselect(".tab-content ul")):
			title = h5.text.strip()
			items = list(map(lambda x: x.text.strip(), ul.cssselect("li")))
			day_menu[title] = items
		menus[day] = day_menu
	return menus

def todays_menu_to_md(menus):
	day = date(2019, 3, 18)
	menu = menus[day]
	
	msg = "🍴 Il menu di oggi _(%s)_\n" % (day.strftime("%A %d %B"))
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

def send_msg(msg, token):
	bot = telepot.Bot(token)
	bot.sendMessage(CHANNEL_ID, msg, parse_mode="Markdown")

def main(token=None):
	menus  = get_menus()
	msg    = todays_menu_to_md(menus)
	send_msg(msg, token)

if __name__ == "__main__":
	main(argv[1])
