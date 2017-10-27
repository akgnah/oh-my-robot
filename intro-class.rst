类、模块和包
==============

类和对象
-----------

面向对象编程有点宏大，在简短的篇幅中我们没有办法去了解很多，这里只是简单地介绍创建和使用类的方法。

我们习惯把相似的事物的相同特征抽象（提取）出来去构建一个类，而类的一个具体实例我们称为对象（下文不区分实例和对象两词）。

对象可以使用属于它的变量来存储数据，这种从属于对象或类的变量叫作字段（field），对象还可以使用属于类的函数来实现某些功能，这种函数叫作类的方法（method）。字段和方法统称为类的属性（attribute）。

我们来看看怎样定义一个类：

.. code-block:: python

   >>> class Auth:
   ...     def __init__(self, consumer):
   ...         self.consumer = consumer
   ...     def request(self, url):
   ...         print(self.consumer)
   ...         print('access url: %s' % url)
   ...
   >>> client = Auth('consumer 1234')
   >>> client.consumer
   'consumer 1234'
   >>> client.request('/statuses/home_timeline')
   consumer 1234
   access url: /statuses/home_timeline
   >>> 

这是 `fanfou-py <https://github.com/akgnah/fanfou-py>`_ （一个访问饭否 API 的包，稍后我们就会安装它）的一个类的简化，
我不想举大多数课本上 People 的例子，但又想不到其他好的例子，考虑到我们这个包以后我们会经常提到，所以使用了这个例子。

使用 class 关键字来创建一个类，类中可以包含字段和方法，其中以 __ 开头和结束（如上面的 __init__）方法是特殊方法，在 Python 中这些方法都有特殊的作用。

如 __init__ 方法我们可以理解为初始化方法，当创建一个类的实例，会先自动调用这方法来做一些初始化工作，在上面我们对属性 consumer 进行了赋值。

__init__ 方法中的第一个参数 self 表示实例本身，它可以为任意名字（如 this），但在 Python 中我们习惯使用 self，如果没有特殊理由要去更改它，那么建议你使用 self。

上面的代码中我们创建了一个 Auth 类，并且创建了一个对象 client。创建对象的方法和调用函数有些类似，把 __init__ 方法中所需要的参数提供给类名即可，像 client = Auth('consumer 1234')。

得到一个对象后，我们就可以查看它的字段或调用它的方法了，访问方式是 对象名.属性名，如 client.consumer 和 client.request('/statuses/home_timeline')。

在方法 request 中，表示对象本身的 self 仍然是它的第一个参数（需和 __init__ 中使用相同的名字），如果写的是对象的方法，那么第一个参数都是指代它本身。
对象的属性会在整个对象中共享，虽然我们在 request 方法没有对 consumer 的定义，但我们仍然可以访问它，访问对象的属性方式是 self.属性名（包括字段和方法）。

我们先来理清一下，在类定义的外部，我们使用变量来表示对象，如 client，而在类定义的内部，我们使用 self 来表示对象，访问属性的方式是一致的，都是 对象.属性 。

一个类可以有不同实例，每个对象都会拥有它们自己的属性，并不会互相干扰：

.. code-block:: python

   >>> client2 = Auth('consumer 5678')
   >>> client2.consumer
   'consumer 5678'
   >>> client.consumer
   'consumer 1234'
   >>> 


还有一种属性叫做类的属性，我们来看看新的 Auth 类：

.. code-block:: python

   >>> class Auth:
   ...     version = '0.1.0'
   ...     def __init__(self, consumer):
   ...         self.consumer = consumer
   ...     def request(self, url):
   ...         print(self.consumer)
   ...         print('access url: %s' % url)
   ... 
   >>> 
   >>> client1 = Auth('test 123')
   >>> client2 = Auth('test 456')
   >>> client1.version
   '0.1.0'
   >>> client2.version
   '0.1.0'
   >>> client1.version = '0.2.0'
   >>> client1.version
   '0.2.0'
   >>> client2.version
   '0.2.0'
   >>> client2.version = '0.2.5'
   >>> client2.version
   '0.2.5'
   >>> client1.version
   '0.2.5'
   >>> 

直接定义在类中的字段我们称为类的属性，类的属性是由它的全部实例共享的，在某一个实例中对类的属性的修改会反映在其他实例身上。我们可以用等号（=）直接对类或对象的属性赋值，即可修改它们。

我们使用类和对象很大一部分是为了代码复用，类的继承是很好的复用手段。

我们编写饭否应用时，在访问饭否 API 前需要认证，而认证有 OAuth 和 XAuth 两种方式。
OAuth 是跳转到饭否的一个页面让你确认登录（如马总的 `物以类聚 <https://marcher.sinaapp.com/>`_ ），而 XAuth 会让我们输入用户名和密码后就直接登录了（如大部分的客户端）。

这两种认证方式有绝大部分操作是相同，所以我们可把相同的部分放在基础的 Auth 类中，然后分别去继承它，下面我们来看看简化的代码：

.. code-block:: python

   >>> class Auth:
   ...     version = '0.1.0'
   ...     def __init__(self, consumer):
   ...         self.consumer = consumer
   ...     def request(self, url):
   ...         print(self.consumer)
   ...         print('access url: %s' % url)
   ...
   >>> class OAuth(Auth):
   ...     def __init__(self, consumer, token):
   ...         Auth.__init__(self, consumer)
   ...         self.token = token
   ...
   >>> class XAuth(Auth):
   ...     def __init__(self, consumer, username, password):
   ...         Auth.__init__(self, consumer)
   ...         self.username = username
   ...         self.password = password
   ... 
   >>> 
   >>> client1 = OAuth('consumer 123', 'token 123')
   >>> client2 = XAuth('consumer 123', 'home2', 'xxxxxx')
   >>> client1.request('/users/show')
   consumer 123
   access url: /users/show
   >>> client2.request('/users/show')
   consumer 123
   access url: /users/show
   >>> 
   
要继承一个类，只需把想要继承的类名放在要创建的类的后面，用圆括号扩住，像 OAuth(Auth) 和 XAuth(Auth)，Auth 称为基类（base class），OAuth 和 XAuth 称为子类（subclass）。

client1 和 client2 分别是 OAuth 和 XAuth 类的一个对象，在它们自己的类定义中并没有 request 方法，但我们却可以调用它。
因为我们继承了 Auth 类，而 Auth 类中定义有 request 方法。

我们来看看子类的 __init__ 方法，在 OAuth 类中，它的 __init__ 方法接受两个参数 consumer 和 token，因为我们继承了 Auth 类，
在做初始化工作的时候我们希望也让基类做一些初始化，所以我们把 consumer 传递给了基类的 __init__ 方法，注意调用基类 __init__ 方法的时候，
self 是第一参数，其后才是想要传递的其他参数。然后我们对自己的属性 token 进行了赋值。XAuth 类的 __init__ 方法也与此类似，只是 XAuth 需要用户名和密码。

子类可以继承基类的属性（包括字段和方法），同时也可以重写（覆盖）它们，我们来看看代码：

.. code-block:: python

   >>> class Auth:
   ...     version = '0.1.0'
   ...     def __init__(self, consumer):
   ...         self.consumer = consumer
   ...     def request(self, url):
   ...         print(self.consumer)
   ...         print('access url: %s' % url)
   ... 
   >>> class OAuth(Auth):
   ...     def __init__(self, consumer, token):
   ...         Auth.__init__(self, consumer)
   ...         self.token = token
   ...     def request(self, url):
   ...         print('OAuth mode')
   ...         print('access url: %s' % url)
   ... 
   >>> class XAuth(Auth):
   ...     def __init__(self, consumer, username, password):
   ...         Auth.__init__(self, consumer)
   ...         self.username = username
   ...         self.password = password
   ...     def request(self, url):
   ...         print('XAuth mode')
   ...         Auth.request(self, url)
   ... 
   >>> 
   >>> client1 = OAuth('consumer 123', 'token 123')
   >>> client2 = XAuth('consumer 123', 'home2', 'xxxxxx')
   >>> client1.request('/users/show')
   OAuth mode
   access url: /users/show
   >>> client2.request('/users/show')
   XAuth mode
   consumer 123
   access url: /users/show
   >>> 

在子类 OAuth 中我们重写了基类 Auth 的 request 方法，打印了 'OAuth mode' 而不是打印 consumer，调用 client1.request('/users/show') 可以看到这种变化。

在子类 XAuth 中我们同重写了 request 方法，打印了 'XAuth mode'，随后我们通过明确指定基类的名字和方法，调用了基类的 request 方法。

上面代码的行为意味着，当我们访问一个对象的属性时，它会首先在本类中查，如果有该属性就使该属性，如果没有再往上往基类查找。
当我们在子类重写了基类的属性时，如果想再次访问基类的属性，需要明确指定基类的名字。

关于类和对象，我们暂且学习到这里，这只是连皮毛都算不上的皮毛，但对我们随后写饭否机器人足够了，如果你想深入了解，要看书或看其他资料喔 ^_^。


模块
-------

我们学会了编写自己的类和函数，它们是代码复用的手段之一，在它们之上的代码复用的方法是模块，把代码保存为以 .py 为后辍的文件即可编写一个模块。

请用文本编辑器输入下面的代码，并保存为 foo.py（以下假设你保存在了 d 盘）：

.. code-block:: python

   x = 1024


   class Bar:
       def hi(self):
           print('foo.py: Bar, hi')


   def func():
       print('foo.py: func')


   def main():
       print('foo.py: main')


   print(x)
   if __name__ == '__main__':
       main()


上面的代码只是简单 print 一些东西，没什么实用意义，只是为了说明模块的用法。现在请打开 命令行提示符，跟着做下面操作：

输入 d: 并按下回车，接着输入 python foo.py 并按下回车，你将会看到 1024 和 'foo.py: main' 被打印在屏幕上，我们稍后再作解释。

现在请输入 python 并按下回车，进入 Python 交互环境：

.. code-block:: python

   >>> import foo
   1024
   >>> foo.x
   1024
   >>> bar = foo.Bar()
   >>> bar.hi()
   foo.py: Bar
   >>> foo.func()
   foo.py: func
   >>> foo.main()
   foo.py: main
   >>> 

我们可以使用 import 文件名（不带 .py 后辍）来导入一个模块，随后即可通过 模块名.成员名 来访问模块的成员，包括变量、类和函数，
如上面的 foo.x、foo.Bar() 和 foo.func() 等。

在导入一个模块的时候，Python 会自动执行一次这个文件，所以我们 import foo 时看到 1024 被打印在屏幕上，而此时我们还没做任何其他操作。

在上面的代码中我们还可以看到，方法__init__ 在创建一个类时不是必须的，如果你无需做初始化工作，你可以不用定义这个方法，Python 会默认提供。

Python 中有个特殊的变量 __name__，常用在编写模块的时，这个变量能辨识这个文件是被作为主文件执行，还是被导入作为模块，
如果是前者，那么 __name__ 的值为 '__main__'，如果是后者，它的值可能是文件名或包名（我们马上会说到包）跟着文件名。

这就是为什么当我们在命令行提示符下执行 python foo.py 的时候，main 会被调用，而导入的时候只打印了 1024。

我们还可以使用 from xx import yy 语句来只导入模块中的某个成员，使用这种格式时访问导的成员不需要加上模块名作为前缀：

.. code-block:: python

   >>> from foo import func
   1024
   >>> func()
   foo.py: func
   >>> 
   
还可以使用 from xx import * 来导入模块中的全部成员，不过强烈不建议这么做，这样做很容易会造成命名混乱。
比如，你从两个模块中这样导入全部成员，而两个模块中刚好有同名的变量或函数，那么后来导入的将会覆盖前面的。

语句 import 和 from xx import yy 后面都可以跟着一个可选的 as 来重新命名，如：

.. code-block:: python

   >>> import foo as f
   1024
   >>> f.x
   1024
   >>> from foo import Bar as B
   >>> b = B()
   >>> b.hi()
   foo.py: Bar
   >>> 
   
使用内置的 dir() 函数可以查看模块的成员，或查看对象的属性，在我们使用别人的模块或类的时候，这个函数很方便地帮我们快速了解：

.. code-block:: python

   >>> import foo
   1024
   >>> dir(foo)
   ['Bar', '__builtins__', '__cached__', '__doc__', '__file__',
   '__loader__', '__name__', '__package__', '__spec__', 'x']
   >>> 


   
包（package）
---------------

包是在模块之上的组织代码的方式，至少包含一个名为 __init__.py 的文件的文件夹就是一个包，文件夹中还可以有其他模块。

下面我们来做一个自己的包，然后结束本章，下章是我们进入正式开发的最后准备。

请在 d 盘新建一个名为 bar 的文件夹，然后新建一个名为 __init__.py 的空白文件，把上一小节的 foo.py 复制进去，这样包就完成了，我们来测试一下。

请打开命令行提示符，输入 d: 并回车切换路径到 d 盘，输入 python 并按下回车：

.. code-block:: python

   >>> from bar import foo
   1024  # 咦，为什么会出现 1024
   >>> foo.x
   1024
   >>> bar = foo.Bar()
   >>> bar.hi()
   foo.py: Bar
   >>> 

我们试试导入整个包：

.. code-block:: python

   >>> import bar
   >>> dir(bar)
   ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
   '__name__', '__package__', '__path__', '__spec__']
   >>> 

咦，foo 哪里去了，按照我们对包的文件层次的直观感觉，导入整个包应该会导入文件夹的模块才对。我们来看点有趣的：

.. code-block:: python

   >>> import bar
   >>> from bar import foo
   1024
   >>> foo.__file__
   'D:\\Code\\bar\\foo.py'
   >>> bar.__file__
   'D:\\Code\\bar\\__init__.py'
   >>> 
   
模块的 __file__ 属性可以记录了模块的文件位置，输入 foo.__file__ 我们得到了 foo 的位置。
你是否会认为 bar.__file__ 应该是 bar 文件夹的位置，但我们得到的是文件夹下的 __init__.py。

看到这里我们应该可以猜测为什么导入整个包的时候，foo 不见了。使用 import bar 时，Python 实际上导入的是 bar 包下的 __init__.py 文件。

那么如果我们想 import bar 时能导入 foo 该怎办，事实上这是很正常的需求。

上面我们新建的 __init__.py 是空白文件，现在请用编辑器打开它，输入下面代码：

.. code-block:: python

   from . import foo

保存文件后请先退出刚才打开的交互环境，再次进入后：

.. code-block:: python

   >>> import bar
   1024
   >>> bar.foo
   <module 'bar.foo' from 'D:\\Code\\bar\\foo.py'>
   >>> dir(bar)
   ['__all__', '__builtins__', '__cached__', '__doc__', '__file__',
   '__loader__', '__name__', '__package__', '__path__', '__spec__', 'foo']
   >>> 

上面添加到 __init__.py 代码中的 . 表示当前目录。这次 foo 出现了，请思考一下为什么会这样？

因为 import bar 的时候导入了 __init__.py 文件，而 __init__.py 导入了 foo.py 文件。

最后我们来看下 import 的时候 Python 能从哪些地方导入模块或包：

.. code-block:: python

   >>> import sys
   >>> sys.path
   ['', 'D:\\Python36\\python36.zip', 'D:\\Python36\\DLLs',
   'D:\\Python36\\lib', 'D:\\Python36', 'D:\\Python36\\lib\\site-packages',
   'D:\\Python36\\lib\\site-packages\\markupsafe-1.0-py3.6-win-amd64.egg']
   >>> 

因为安装路径的不同，你得到的结果可能和我不同。sys.path 保存着 Python 导入时会查找的路径，它是一个列表，列表的首项是空字符串，空字符串代表的是当前目录。

因为 sys.path 是一个列表，所以你应该能想到如果想增加查找路径应该怎样做。

包和模块我们统称为库。

这章到这里结束了，下章我们将学习怎样实际去访问饭否 API。
