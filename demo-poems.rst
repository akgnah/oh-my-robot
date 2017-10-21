Demo：诗词君
================

诗词君每天会向参与的饭友随机推送一句诗词。这里有两个问题要考虑的，1、如何记录参与的饭友；2、如何随机选取一句诗词。


知识准备
----------

永久记录数据一般有两种方式，保存到磁盘或数据库上，前者比较简单，所以我们采取文件的形式。

我们来看看在 Python 中如何读写文件，为了方便，请先在 cmd 切换到 d 盘后，输入 python 进入交互环境：

.. code-block:: python

   >>> f = open('test.txt')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
   >>> 
   
当你尝试打开一个不存在的文件的时候，会得到错误信息。我们先来创建文件：

.. code-block:: python

   >>> f = open('test.txt', 'w')
   >>> f.write('hello, fanfou')
   >>> f.close()
   >>> 

现在打开文件浏览器，看是否有一个 test.txt 的文件，可以打开查看它的内容。

内置函数 open() 可以打开一个文件，上面两次的函数调用的区别在于，第二次多传递了一个参数 'w'，
这个字符代表着打开文件的模式，可用模式如下表：

  =========    ===============================================================
  字符          含义
  ---------    ---------------------------------------------------------------
  'r'          读取（默认），如果文件不存在则失败
  'w'          写入，如果文件已存在则先清空原文件
  'x'          创建新文件并写入，如果文件已存在则失败
  'a'          写入，如果文件已存在则追加到文件的末端
  'b'          二进制模式，需和 r/w/x/a 中的一个共同使用
  't'          文本模式（默认），需和 r/w/x/a 中的一个共使用
  '+'          读取和写入，和 r/w/x/a 中的一个共同使用
  'U'          通用换行模式（已弃用）
  =========    ===============================================================


默认的模式是 'rt'（读取文本文件）。得到一个文件对象后，将有一些方法可使用，如上面的 write()。

请下载 `poems.txt <code/poems.txt>`_ 到你的 d 盘，我们接着看代码：

.. code-block:: python

   >>> f = open('poems.txt', encoding='utf8')
   >>> poems = f.readlines()
   >>> len(poems)
   952
   >>> type(poems)
   <class 'list'>
   >>> poems[0]
   '曲则全，枉则直。（《老子》）\n'
   >>> poems[1]
   '言必信，行必果。（《论语》）\n'
   >>> 

我把收集到的诗词一行一句保存在 poems.txt，在上面我们以读取文本模式打开了它，并把 f.readlines() 返回的结果赋值给 poems。
这是一个列表，每个元素都是一句诗词，这离我们解决问题近了一步，接下来只要想办法每次随机选取一句即可。

我们来看看怎样随机选取元素：

.. code-block:: python

   >>> import random
   >>> arr = [1, 2, 3, 4, 5, 6]
   >>> random.chioce(arr)
   3
   >>> random.chioce(arr)
   6
   >>> random.chioce(arr)
   2
   >>>

你会发现你得到的结果和我不同，因为 random.choice() 的作用是在列表中随机选取一个元素。那么我们把 random.choice() 应用在 poems 上即可随机选取诗词。

接下来我们看看怎样记录参与的饭友，这需要用到另一个标准库 shelve：

.. code-block:: python

   >>> import shelve
   >>> db = shelve.open('poems.dbm')
   >>> db['test'] = 'hello, fanfou'
   >>> 

现在请退出交互环境并去 d 盘查看是否有 poems.dbm 等文件，如果有我们再次进入交互环境：

.. code-block:: python

   >>> import shelve
   >>> db = shelve.open('poems.dbm')
   >>> db['test']
   'hello, fanfou'
   >>> list(db.keys())
   ['test']
   >>> 
   

你看，它把我们刚才的赋值保存起来了，你可以像一个字典一样来使用 shelve 返回的对象 db，我们对它的修改会自动保存到磁盘上。


开始工作
----------

我们已经解决了最初需要考虑的两个问题，现在来看看怎样让诗词君工作起来。

检查 mentions
^^^^^^^^^^^^^^^^

我们需要访问 mentions 的消息，看是否有想要加入或退出的饭否，然后更新到我们的 db 上：

.. code-block:: python

   import fanfou

   # 请修改为你的 Consumer
   consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
   # 请修改为你的 ID 和密码
   client = fanfou.XAuth(consumer, 'username', 'password')
   fanfou.bound(client)

   resp = client.statuses.mentions()

   for item in resp.json():
       user_id = item['user']['unique_id']
       if '-join' in item['text']:
	   db[user_id] = item['user']['name']
       elif '-quit' in item['text']:
	   try:
	       del db[user_id]
	   except:
	       pass

	
更新名字
^^^^^^^^^^

参与推送的饭友有时候可能会改名，而改名了我们就 at 不到，所以需要定时更新名字：

.. code-block:: python

   import time

   for user_id in db.keys():
       try:
           resp = client.users.show({'id': user_id})
           db[user_id] = resp.json()['name']
       except:
           pass
       time.sleep(0.5)


推送诗词
^^^^^^^^^^

终于到推送这一步啦：

.. code-block:: python

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

放在一起
^^^^^^^^^^

定时执行的方法我们在上一个 Demo 已经学习了，把上面这些东西放在一起，我们的诗词君就完成了。完整的代码可点击 `poems.py <code/poems.py>`_ 查看 。
