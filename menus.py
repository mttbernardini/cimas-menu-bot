#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Matteo Bernardini

import requests, locale, lxml.html
from sys import argv, stdout
from datetime import datetime

# altrimenti non parsa i mesi in italiano
locale.setlocale(locale.LC_TIME, ("it_IT", "UTF-8"))

MENU_URL = "http://www.cimasristorazione.com/menu-mense/universita-roma-3/"

def getMenus():
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
