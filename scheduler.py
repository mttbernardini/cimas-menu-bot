#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Matteo Bernardini

from apscheduler.schedulers.blocking import BlockingScheduler
from sys import argv
import cimas_bot

sched = BlockingScheduler()

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=22, minute=32)
def scheduled_job():
    cimas_bot.main()

print("scheduler started")
sched.start()
