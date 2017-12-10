#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import random
import shelve
import datetime
import fanfou

# 请修改为你的 Consumer
consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
# 请修改为你的 ID 和密码
client = fanfou.XAuth(consumer, 'username', 'password')
fanfou.bound(client)

with open('poems.txt', encoding='utf8') as f:
    poems = f.readlines()

db = shelve.open('poems.dbm')


def check():
    try:
        resp = client.statuses.mentions()
    except:
        return
    for item in resp.json():
        user_id = item['user']['unique_id']
        if '-join' in item['text']:
            db[user_id] = item['user']['name']
        elif '-quit' in item['text']:
            try:
                del db[user_id]
            except:
                pass


def update():
    for user_id in db.keys():
        try:
            resp = client.users.show({'id': user_id})
            db[user_id] = resp.json()['name']
        except:
            pass
        time.sleep(0.5)


def send():
    for user_id, name in db.items():
        try:
            poem = random.choice(poems).strip()
            body = {
                'status': '@%s %s' % (name, poem),
                'in_reply_to_user_id': user_id,
            }
            client.statuses.update(body)
        except:
            pass
        time.sleep(0.5)


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute < 1:
            send()
        elif now.hour == 4 and now.minute < 1:
            update()
        elif now.minute % 15 == 0:
            check()
        time.sleep(60)
