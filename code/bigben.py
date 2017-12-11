#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import fanfou

# 请修改为你的 Consumer
consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
# 请修改为你的 ID 和密码
client = fanfou.XAuth(consumer, 'username', 'password')
fanfou.bound(client)

now = datetime.datetime.now()
bong = 'Bong ' * ((now.hour % 12) or 12)
client.statuses.update({'status': bong[:-1] + '!'})
