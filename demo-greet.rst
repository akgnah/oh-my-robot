Demo：小鲸鱼
===============

小鲸鱼（ `@Mr.Greeting <https://fanfou.com/testbytse>`_ ）是一个早晚安问候机器人。

请确保了你看了前面两个 Demo，有些知识在前面学习过而在这里直接使用。为了简化，Demo 中只进行了晚上的问候。

下面我们直接看代码：

.. code-block:: python

   import time
   import random
   import shelve
   import fanfou  

   # 请修改为你的 Consumer
   consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
   # 请修改为你的 ID 和密码
   client = fanfou.XAuth(consumer, 'username', 'password')
   fanfou.bound(client)

   db = shelve.open('greet.dbm')
   kw_words = ['晚安', '好梦', 'Good night', 'Good Night',
		'good night', 'お休みなさい', 'おやすみなさい']
   reply_words = ['Good night~', 'Sweet dream~',
		'おやすみなさい～', '晚安～', '晚安哦～']

   resp = client.statuses.home_timeline()

   for item in resp.json():
       status_id = item['id']
       if status_id in db.keys():
           continue

       for kw in kw_words:
           if kw in item['text']:
	       reply = random.choice(reply_words)
	       status = '%s 转@%s %s' % (reply, item['user']['name'], item['text'])
	       body = {'status': status, 'repost_status_id': status_id}
	       try:
	           client.statuses.update(body)
		   break
	       except:
	           pass
	       db[status_id] = True
	       
上面的代码都是我们学习过的，需要提的一点是，已经转发了的消息我们把需要把 id 加入 db 中，这样才不会造成重复转发。完整的代码可以点击 `greeting.py <code/greeting.py>`_ 查看。


教程中的 Demo 机器人简化了一些情况，这是为了方便讲解。现在正在运行的诗词君和小鲸鱼的代码可在 `fanfou-bot <https://github.com/akgnah/fanfou-bot>`_ 中找到，你会发现并没有复杂多少，大体结构和我们的 Demo 很相似。

去动手写你的机器人吧，写好记得告诉我喔 ^_^ 。
