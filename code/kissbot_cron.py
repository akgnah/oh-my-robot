#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import fanfou


consumer = {'key': 'consumer key', 'secret': 'consumer secret'}  # 请修改为你的 Consumer
client = fanfou.XAuth(consumer, 'username', 'password')  # 请修改为你的 ID 和密码
fanfou.bound(client)


def work():
    last = client.statuses.update({'status': time.time()}).json()['id']
    time.sleep(0.5)

    user = {'id': 'home2'}  # 请修改为你想要 at 的饭友的ID
    name = client.users.show(user).json()['name']
    time.sleep(0.5)

    body = {'status': '@%s 么么哒～' % name, 'in_reply_to_user_id': user['id']}
    client.statuses.update(body)
    time.sleep(0.5)

    client.statuses.destroy({'id': last})


while True:
    now = datetime.datetime.now()
    if now.hour in (6, 22) and now.minute < 1:
        try:
            work()
        except:
            pass    # pass 是什么都不做的意思
    time.sleep(60)
