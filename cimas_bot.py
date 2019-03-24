#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Gianmaria Del Monte

import telepot

TOKEN='633120718:AAGPAeiYo7xWwAdM9lGeG0GotmGlzJXQ8QQ'
CHANNEL_ID = -1001186126012

def send_msg(msg):
	bot = telepot.Bot(TOKEN)
	bot.sendMessage(CHANNEL_ID, msg)

if __name__ == '__main__':
	send_msg()
