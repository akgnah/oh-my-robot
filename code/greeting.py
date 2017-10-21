#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import random
import shelve
import datetime
import fanfou

consumer = {'key': 'consumer key', 'secret': 'consumer secret'}  # 请修改为你的 Consumer
client = fanfou.XAuth(consumer, 'username', 'password')  # 请修改为你的 ID 和密码
fanfou.bound(client)


db = shelve.open('greet.dbm')
kw_words = ['晚安', '好梦', 'Good night', 'Good Night', 'good night', 'お休みなさい', 'おやすみなさい']
reply_words = ['Good night~', 'Sweet dream~', 'おやすみなさい～', '晚安～', '晚安哦～']


def work():
    resp = client.statuses.home_timeline()
    for item in resp.json():
        status_id = item['id']
        if status_id in db.keys():
            continue

        for kw in kw_words:
            if kw in item['text']:
                db[status_id] = True
                send(item)
                break


def send(item):
    reply = random.choice(reply_words)
    status = '%s 转@%s %s' % (reply, item['user']['name'], item['text'])
    body = {'status': status, 'repost_status_id': item['id']}

    try:
        client.statuses.update(body)
    except:
        pass


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        if now.hour in [22, 23, 0]:
            try:
                work()
            except:
                pass
        time.sleep(60)
