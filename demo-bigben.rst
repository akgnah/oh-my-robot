Demo：小本钟
===============

发现 `@大本钟 <https://fanfou.com/大本钟>`_ 好像休假了，于是我写了 `@小本钟 <https://fanfou.com/tinyben>`_ 去替班，
这应该是饭否上最简单的机器人之一，前后动手到上线不到三分钟（没错，Python 就是这么棒），下面我们直接来看代码（ `bigben.py <code/bigben.py>`_ ）吧：

.. code-block:: python

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
   bong = 'Bong ' * ((now.hour % 12) or 1)
   client.statuses.update({'status': bong[:-1] + '!'})


看，包括注释不到 20 行代码，我们就可以完成一个饭否机器人。

请确保你修改了上面需要修改的地方，然后 python bigben.py 这样运行它。然后去饭否查看效果吧。

我们用到了一个新的模块 datetime，这是一个处理日期和时间的模块。在上面我们获取了当前时间 now，它返回一个对象，可以直接访问它的属性（如 day，hour 和 minute 等）。
机器人报时会发送和当前点数相同个数的 Bong，所以需要使用 now.hour（0 <= now.hour < 24）去计算 Bong 的个数。


`@大本钟 <https://fanfou.com/大本钟>`_ 整点报时全年午休，这当然不是手动执行的，我们需要一个定时执行的功能。如果你在使用 Linux，那么最简单的方式是使用 Crontab。

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
   

模块 time 包含了另一些常用的时间操作，比如休眠（time.sleep(x)，x 为一个以秒为单位的数），
你会发现上面的代码每隔 5 秒就会在屏幕打印 hello，请按下 Ctrl + C 或点击窗口关闭按钮来关闭它。
如果你不这么做，那么它将会一直运行下去，我们在上一章说过，while 可以重复执行块内的代码，直到判断条件为假时才结束。
看了上面的例子，你应该猜到了让代码定时运行的方法，把代码放到一个永真循环中，执行代码并休眠（sleep）一段时间。

机器人每个整点报时，为了达到这个效果我们还要做点其他工作：

.. code-block:: python

   >>> import datetime
   >>> now = datetime.datetime.now()
   >>> now
   datetime.datetime(2017, 12, 10, 23, 31, 2, 998078)
   >>> now.hour
   23
   >>> now.minute
   31
   >>> 


有了这些，我们可以真的定时来执行一些任务了，下面是大概的模型：

.. code-block:: python

   >>> import time
   >>> import datetime
   >>> def work():
   ...     print('do something')
   ... 
   >>> while True:
   ...     now = datetime.datetime.now()
   ...     if now.minute < 1:
   ...         work()
   ...     time.sleep(60)
   ... 

你只需要把你实际想做的工作放在函数 work 中即可，运行它，它会一直运行，并在恰当的时候执行 work。完整的可定时执行的机器人代码可点击 `bigben2.py <code/bigben2.py>`_ 查看。
