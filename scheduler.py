#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Matteo Bernardini

from apscheduler.schedulers.blocking import BlockingScheduler
import menus

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=12)
def scheduled_job():
    menus.getMenus()

print("scheduler started")
sched.start()
