#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Gianmaria Del Monte

from flask import Flask
import cimas_bot

app = Flask(__name__)

@app.route("/")
def hello():
	msg = "Hello world from Flask!"
	bot_tg.send_msg(msg)
	return "Hello World!"
