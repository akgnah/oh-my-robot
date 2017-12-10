#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import fanfou


# 请修改为你的 Consumer
consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
# 请修改为你的 ID 和密码
client = fanfou.XAuth(consumer, 'username', 'password')
fanfou.bound(client)


def work():
    now = datetime.datetime.now()
    bong = 'Bong ' * ((now.hour % 12) or 1)
    client.statuses.update({'status': bong[:-1] + '!'})


while True:
    now = datetime.datetime.now()
    if now.minute < 1:
        try:
            work()
        except:
            pass    # pass 表示什么都不做
    time.sleep(60)
