#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Matteo Bernardini

from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
import cimas_bot

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    cimas_bot.main(environ["TG_TOKEN"])

print("scheduler started")
sched.start()
