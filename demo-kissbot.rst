Demo：亲吻君
===============

去年 6 月的时候，TL（Timeline）上有个很甜很可爱的小姐姐，说喜欢别人对她说么么哒，我看到后就写了这个么么哒机器人 `@偏咸 <https://fanfou.com/bot.>`_ ，
这应该是饭否上最简单的机器人之一，前后动手到上线不到十分钟（没错，Python 就是这么棒），下面我们直接来看代码（ `kissbot.py <code/kissbot.py>`_ ）吧：

.. code-block:: python

   #!/usr/bin/python
   # -*- coding: utf-8 -*-
   import time
   import fanfou

   # 请修改为你的 Consumer
   consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
   # 请修改为你的 ID 和密码
   client = fanfou.XAuth(consumer, 'username', 'password')
   fanfou.bound(client)

   # 发送一个时间戳，并记住该消息的 ID
   last = client.statuses.update({'status': time.time()}).json()['id']
   time.sleep(0.5)  # 休眠一下，避免频繁请求 API 造成失败，下同

   # 获取用户的名字，因为对方有可能会修改名字
   user = {'id': 'home2'}  # 请修改为你想要 at 的饭友的ID
   name = client.users.show(user).json()['name']
   time.sleep(0.5)

   # 发送 么么哒～
   body = {'status': '@%s 么么哒～' % name, 'in_reply_to_user_id': user['id']}
   client.statuses.update(body)
   time.sleep(0.5)

   # 删除刚才发送的时间戳
   client.statuses.destroy({'id': last})


看，包括注释不到 30 行代码，我们就可以完成一个饭否机器人。

请确保你修改了上面需要修改的地方，然后 python kissbot.py 这样运行它。然后去饭否查看效果吧。

在上面我们用到了一个新的模块 time，这个模块包含一些常用的时间操作，比如休眠（time.sleep(x)，x 为一个以秒为单位的数）和获得当前时间戳（time.time()）。

由于饭否不允许连续发两条重复的消息，我们先发送时间戳随后再删除来绕过这个限制，所以么么哒机器人可以全屏都是么么哒。

如果你点开了我的 `么么哒机器人 <https://fanfou.com/bot.>`_ ，你会发现它每天都自动发送两次消息，这当然不是我手动执行的，这时我们需要一个定时执行的功能。如果你在使用 Linux，那么最简单的方式是使用 Crontab。

如果你在使用 Windows，那么我们来看看怎样用 Python 自己的方法来定时执行：

.. code-block:: python

   >>> import time
   >>> while True:
   ...     print('hello')
   ...     time.sleep(5)
   ... 
   hello
   hello
   hello
   hello
   

你会发现上面的代码每隔 5 秒就会在屏幕打印 hello，请按下 Ctrl + C 或点击窗口关闭按钮来关闭它。
如果你不这么做，那么它将会一直运行下去，我们在上一章说过，while 可以重复执行块内的代码，直到判断条件为假时才结束。
看了上面的例子，你应该猜到了让代码定时运行的方法，把代码放到一个永真循环中，执行代码并休眠（sleep）一段时间。

在么么哒机器人中，他每天早上六点和晚上十点发送消息，为了达到这个效果我们还要做点其他工作：

.. code-block:: python

   >>> import datetime
   >>> now = datetime.datetime.now()
   >>> now
   datetime.datetime(2017, 10, 14, 16, 23, 14, 87958)
   >>> now.hour
   16
   >>> now.minute
   23
   >>> 

datetime 是另一个处理日期和时间的模块，有些功能比 time 中的方便，比如我们上面获取现在的时间 now，它返回的是一个对象，可以直接访问它的属性（如 day，hour 和 minute 等）。

有了这些，我们可以真的定时来执行一些任务了，下面是大概的模型：

.. code-block:: python

   >>> import time
   >>> import datetime
   >>> def work():
   ...     print('do something')
   ... 
   >>> while True:
   ...     now = datetime.datetime.now()
   ...     if now.hour in (6, 22) and now.minute < 1:
   ...         work()
   ...     time.sleep(60)


你只需要把你实际想做的工作放在函数 work 中即可，运行它，它会一直运行，并在恰当的时候执行 work。完整的可定时执行机器人的代码可点击 `kissbot_cron.py <code/kissbot_cron.py>`_ 查看。
