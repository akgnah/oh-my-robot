控制流和函数
==============


流程控制
----------

我们在真正写程序时，代码大多不是从头到尾顺序执行的，我们会希望对一些情况作出判断，并执行相应的操作，还会希望可以重复执行一段代码。流程控制正是满足这种需求的东西，包括分支选择以及循环结构。

这里要提一下在 Python 中十分重要的东西，Python 使用缩进来区分代码块，一般向右缩进 4 个空格表示子块。

请分别在交互环境和文件中尝试这些代码，这样你会对使用缩进区分代码块更加理解。请注意，>>> 和 ... 是交互环境的提示符，在文件中你不用输入它。

分支选择
^^^^^^^^^^^

我们可以使用 if else elif 来对代码做出分支选择，就像下面这样：

.. code-block:: python

   >>> n = input('please enter a number: ')
   please enter a number: 12  # 请从键盘输入一个数字，这里我输入了 12 并按下回车
   >>> type(n)
   <class 'str'>
   >>> n = int(n)
   >>> if n > 10:
   ...     print('n > 10')
   ... elif n == 10:
   ...     print('emmm')
   ...     print('n == 10')
   ... else:
   ...     print('n < 10')
   ... 
   n > 10
   >>> 

内置函数 input() 能在键盘中获得输入，需要注意的是，即使你输入的是键盘上数字，它获得的结果也是字符串，如果我们想要的是数字，那么需要转换一下。

在上面的代码中，我们还看到了 3 个新的关键字，if、elif 和 else，其中的 elif 是 else if 的意思。

凡是能得到布尔值的表达试都能放到 if 或 elif 后面，当表达式为真则执行对应的代码块（比它更向右缩进的块），并跳出该选择结构，如果都为假则执行 else 对应的代码块。

在一个分支选择结构中，elif 和 else 都是可选的，可出现多个 elif，多个结构还可以嵌套地使用。


循环结构
^^^^^^^^^^^

Python 有 for 和 while 两种循环结构，先来看看 while 循环：

.. code-block:: python

   >>> a = 0
   >>> while a < 5:
   ...     print(a)
   ...     a = a + 1
   ... 
   0
   1
   2
   3
   4
   >>> 

把一个可判断布尔值的表达式放在 while 后面，为真时则执行循环体内的代码，我们一般还会在循环体内修改判断某个值，以让最终循环会顺利结束，上例中每次循环都让 a 增加 1（a = a + 1）。

现在我们来看看 for 循环：

.. code-block:: python

   >>> bar = [0, 1, 2, 3, 4]
   >>> for x in bar:
   ...     print(x)
   ... 
   0
   1
   2
   3
   4
   >>> for i in range(5):
   ...     print(i)
   ... 
   0
   1
   2
   3
   4
   >>> for c in 'fanfou':
   ...     print(c)
   ... 
   f
   a
   n
   f
   o
   u
   >>> 

for 循环可遍历一个序列（字符串、列表和元组等），并每次把得到的元素赋值给 for 和 in 中间的变量（在上面分别是 x、i 和 c），这样你就可以在循环体内使用这个值了。

请注意，第一和第二个例子产生了同样的结果，这是因为内置函数 range() 能生成一个序列，你可以提供给这个函数起点和终点（还可以提供步进），它会生成一个数字序列。

函数 range() 生成的序列不包括终点，因为起点默认是 0，所以你可以只简单地提供终点，range(5) 和 range(0, 5) 以及 range(0, 5, 1) 等价。

我们再来看些复杂点的情况：

.. code-block:: python

   >>> for i in range(0, 10, 2):
   ...     print(i)
   ... 
   0
   2
   4
   6
   8
   >>> for i in range(5, 0, -1):
   ...     print(i)
   ... 
   5
   4
   3
   2
   1
   >>> 

第一个例子打印了 10 以内的偶数，以为我们给 range 提供了步进 2，它会每次前进 2 步；在第二个例子中，我们从大到小打印了 5 到 1，步进 -1 会让它每次后退一步，
同时它打印了 5 而没有打印 0，上面我们说过了 range 不包括终点。是否觉得和切片的规则类似，是的，它们的规则是一致的。

我们再来看看 continue 和 break：

.. code-block:: python

   >>> for i in range(10):
   ...     if i % 2 == 1:
   ...         continue
   ...     print(i)
   ... 
   0
   2
   4
   6
   8
   >>> for i in range(10):
   ...     if i >= 5:
   ...         break
   ...     print(i)
   ... 
   0
   1
   2
   3
   4
   >>> 

continue 可以跳过某一次循环，而 break 可以跳出整个循环。

提醒一下，如果在多重循环中，break 只会跳出当层循环，而不会跳出全部循环。continue 也是这样，只会跳过当层某一次循环。


异常捕获
^^^^^^^^^^

Python 在遇到异常时默认会退出程序，我们可以使用异常捕获来改变这个行为，所以我们也放在流程控制这节来说明。

来看一下什么是异常：

.. code-block:: python

   >>> '10' + 5
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: must be str, not int
   >>> 4 / 0
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ZeroDivisionError: division by zero
   >>> arr = [1, 2, 3]
   >>> arr[4]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range
   >>> 

上面这些都是异常，当 Python 遇到错误时就会抛出异常。我们来看看更具体的例子：

.. code-block:: python

   >>> arr = [1, 'home', 6, 7]
   >>> for x in arr:
   ...     print(x + 2)
   ... 
   3
   Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
   TypeError: must be str, not int
   >>> 

在上面的代码中我们想打印列表中每个元素和 2 相加的结果，但混进了字符串，在第二次循环就遇到异常而退出。

让我们来改善一下代码，让它遇到字符串时也能工作，这时候有两种方法，我们先来看第一种：

.. code-block:: python

   >>> arr = [1, 'home', 6, 7]
   >>> for x in arr:
   ...     if type(x) is str:
   ...         print(x + '2')
   ...     else:
   ...         print(x + 2)
   ... 
   3
   home2
   8
   9
   >>> 

可以看到它如期工作了。我们再来看第二种方式：

.. code-block:: python

   >>> arr = [1, 'home', 6, 7]
   >>> for x in arr:
   ...     try:
   ...         print(x + 2)
   ...     except TypeError:
   ...         print(x + '2')
   ... 
   3
   home2
   8
   9
   >>> 

这就是异常捕获，把可能出错的代码放在 try 块内，用 except 去捕获可能的异常，然后执行相应的代码。

可以捕获多种异常，也可以捕获全部的异常。异常捕获还有一个可选的 finally 块，不管有没有出错它都会执行。

我们再来看一个例子：

.. code-block:: python

   >>> arr = [2, 3, 0, 'home2']
   >>> for x in arr:
   ...     try:
   ...         print(100 / x)
   ...     except TypeError as e:
   ...         print(e)
   ...     except ZeroDivisionError as e:
   ...         print(e)
   ...     except Exception as e:
   ...         print(e)
   ... 
   50.0
   33.333333333333336
   division by zero
   unsupported operand type(s) for /: 'int' and 'str'
   >>> 


上面的代码中，我们捕获了两种不同异常，还捕获了全部的异常 Exception。如果异常没有被前面 except 语句捕获到的话，那么它将进入 Exception 这块，类似分支选择的 else。 

在 Python 中，我们更推荐使用异常捕获，因为太多的条件判断会影响代码清晰度。就让它去浪吧，出差错了我们捞一下就好（ `EAFP <https://docs.python.org/3/glossary.html#term-eafp>`_ ）。


函数
-------

函数（function）是指可重复使用的程序片段，可通过被赋予的名字来重复调用。前面我们已经使用过一些内置的函数，例如 print()，len() 和 range()。

定义函数
^^^^^^^^^^

我们同样可以定义自己的函数并在需要的地方调用它：

.. code-block:: python

   >>> def add(x, y):
   ...     print(x + y)
   ... 
   >>> add(3, 5)
   8
   >>> 

在上面的代码中，我们定义了一个 add 函数，给它传递两个数将会打印它们的和，注意到我们在 add 里面使用 print，这意味着可以在函数中调用另一个函数（其实也可以调用自身，稍后我们会看到）。

对于一个结果，有时候我们并不想打印它而是想获得它，这时候可以用 return 来返回，如果没有明确指定 return，那么函数会返回 None：

.. code-block:: python

   >>> def mul(x, y):
   ...     return x * y
   ...
   >>> mul(3, 5)
   15
   >>> print(mul(3, 5))
   15
   >>> print(add(3, 5))
   None
   >>> 

在交互环境中看不出差别，因为在交互环境中 Python 会自动打印返回的值。如果用文件的方式运行上面的代码，则会看到只有一个 15 被打印到屏幕。

请注意到这一行 print(mul(3, 5))，你会发现函数可以嵌套调用，也能发现函数调用会由里向外展开，先得到 mul(3, 5) 的结果 15，再把它传递给 print()，于是 15 被打印出来了。

我们来看看函数调用自身，这是一个计算阶乘（n!）的代码：

.. code-block:: python

   >>> def fact(n):
   ...     if n == 1 or n == 0:
   ...         return 1
   ...     else:
   ...         return n * fact(n - 1)
   ... 
   >>> fact(3)
   6
   >>> fact(5)
   120
   >>> 

代码中都是我们学过的东西，对于 fact(3)，你能描述它的计算过程吗？它的计算过程如下：

::

   ==> fact(3)
   ==> 3 * fact(2)
   ==> 3 * (2 * fact(1))
   ==> 3 * (2 * 1)
   ==> 3 * 2
   ==> 6

你会看到它先展开再归约。这种在体内调用自身的函数叫做递归函数，它的优点是定义简单，逻辑清晰。


匿名函数
^^^^^^^^^^

有时候你可能想临时写一个小函数，但又不想给它命名，这时我们可以使用关键字 lambda 来定义匿名函数：

.. code-block:: python

   >>> (lambda x: x * x)(5)
   25
   >>> 

我们提供了参数 5 并立即得到了结果。虽说是匿名函数，但它同样可以赋值给变量：

.. code-block:: python

   >>> f = lambda x: x ** 3
   >>> f(5)
   125
   >>> 

本来本着最小代价的原则，打算省略 **列表推导式** 不说（因为 Demo 机器人没用到它嘛），但不说这个，匿名函数的用法不好举例子。

所以我们先来看看列表推导式吧：

.. code-block:: python

   >>> arr = range(5)
   >>> arr
   range(0, 5)
   >>> list(arr)
   [0, 1, 2, 3, 4]
   >>> [x for x in arr]
   [0, 1, 2, 3, 4]
   >>> 

上面代码中最后一句就是列表推导式，它和 for 循环有些像，只是被包括在中括号中。

你可能会疑惑，既然 list() 可以把一个 range 对象转换列表，那么为什么要用看着那么复杂的列表推导式，做着同样的事。

下面神奇的事情来了，请把喵抱在腿上以免过于惊吓：

.. code-block:: python

   >>> arr = range(5)
   >>> list(arr)
   [0, 1, 2, 3, 4]
   >>> [x + 1 for x in arr]
   [1, 2, 3, 4, 5]
   >>> [x * 2 for x in arr]
   [0, 2, 4, 6, 8]
   >>> [x ** x for x in arr]
   [1, 1, 4, 27, 256]
   >>> [x for x in arr if x % 2 == 0]
   [0, 2, 4]
   >>> 

列表推导式可以把规则应用在原列表身上，以生成新的列表，同时还可以过滤元素。

但是，这个和匿名函数有关系吗？（而且我也没有受到惊吓，你边抚摸喵边喃喃道）

是这样的，除了使用列表推导式，我们还可以使用内置函数 map() 和 filter() 配合着匿名函数来完成上面的操作。在非常大的序列上面，听说这样做的效率会高一些（反正我更喜欢使用列表推导式）。

下面我们来看看匿名函数的版本：

.. code-block:: python

   >>> arr = range(5)
   >>> list(arr)
   [0, 1, 2, 3, 4]
   >>> map(lambda x: x + 1, arr)
   <map object at 0x7fe1259f2eb8>
   >>> list(map(lambda x: x + 1, arr))
   [1, 2, 3, 4, 5]
   >>> list(map(lambda x: x * 2, arr))
   [0, 2, 4, 6, 8]
   >>> list(map(lambda x: x ** x, arr))
   [1, 1, 4, 27, 256]
   >>> list(filter(lambda x: x % 2 == 0, arr))
   [0, 2, 4]
   >>> 

调用 map() 后发现返回的是 map 对象，它是可迭代对象，为了查看结果我们直接把它转换成列表。

还有其他的匿名函数应用场景，以及还有字典和生成器推导式，我就不说啦，感兴趣的话我们后面找本书来看一下喔 ^_^。


形参与作用域
^^^^^^^^^^^^^^

现在我们需要来看看函数的参数，并讨论下变量的作用域。

这个小节可能有点不好理解，如果你看了几遍还是不太懂，那都是我的错，是我没能把事情讲清楚，如果需要帮助请在饭否上联系我（ `@home2 <https://fanfou.com/home2>`_ ）。

上面我们说了，定义函数使用关键字 def，后面紧跟着的名字用于标识这个函数（如上面的 add 和 mul），接着是一对圆括号。

括号中可以有零个或多个表示形参（parameters）的名字，调用函数时我们传递给函数的值（values）称为实参（arguments）。

在函数的执行过程中，形参和实参会进行临时绑定，这个绑定在仅该函数体内有效。

最后的效果看起来就像我们替换了函数体内的形参，进行了运算并得到结果：

.. code-block:: python

   >>> def hello(name):
   ...     print(name)
   ...
   >>> hello('fanfou')
   fanfou
   >>> name
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'name' is not defined
   >>> 

当我们在 hello 外面输入 name 的时候，我们得到了一个错误提示，名字 'name' 没有定义，这是因为形参 name 仅在 hello 体内有效，这和局部变量很相似（下面我们会说到）：

.. code-block:: python

   >>> name = 'Mr.G'
   >>> name
   'Mr.G'
   >>> def hello1():
   ...     print(name)
   ...
   >>> def hello2(name):
   ...     print(name)
   ...
   >>> hello1()
   Mr.G
   >>> hello2('fanfou')
   fanfou
   >>> 

我们先定义了一个名为 name 的全局变量 （global variables），然后定义两个不同的 hello 函数，他们的区别是前者不接受参数。

调用 hello1 的时候会在屏幕打印 Mr.G，而调用 hello2 的时候会打印传递给它的 'fanfou'，而不是打印外面的 name（'Mr.G'）。

这意味着 Python 查找变量的值会由近到远，在 hello2 中，name 绑定到了我们传递的 'fanfou'，那么将会使用这个值并打印出来，
而在 hello1 中，因为函数体内没有 name 这个变量，那么就会再往外面寻找。

我们再来看一个明显点的例子，顺便说一下局部变量（local variables）：

.. code-block:: python

   >>> name = 'Mr.G'
   >>> name
   'Mr.G'
   >>> def hello3():
   ...     name = 'cat'
   ...     print(name)
   ...
   >>> hello3()
   cat
   >>> name
   'Mr.G'
   >>> 

我们在定义了全局变量 name 后又在 hello3 体内定义了同名的局部变量 name，当执行 hello3 的时候，cat 被打印到了屏幕，而在外面我们再次测试 name 的值，得到了 'Mr.G'。

这意味着在 hello3 对变量 name 的赋值仅在 hello3 体内有效，而不会修改外面 name 的值（'Mr.G'）。

当然有方法可以改变这种行为，但我们不常用，因为容易造成变量的混乱：

.. code-block:: python

   >>> name = 'Mr.G'
   >>> name
   'Mr.G'
   >>> def hello4():
   ...     global name
   ...     name = 'cat'
   ...
   >>> name
   'Mr.G'
   >>> hello4()
   'cat'
   >>> name
   'cat'
   >>> 

在一个代码块内（比如函数体内），我们可以使用关键字 global 把一个变量变成全局变量，之后对这个变量的修改也会反映在外面的变量上面。

上面的代码还让我们看到，当我们定义一个函数的时候，函数体内的代码并不会执行，直到我们调用它的时候才执行。

所以我们在调用 hello4 之前，name 的值还是 'Mr.G'，之后之后才修改了它的值，变成了 'cat'。


Python 函数的参数十分灵活，包括默认参数，关键字参数，可变参数：

.. code-block:: python

   >>> def hi(name='home2'):
   ...     print('hi, ' + name)
   ...
   >>> hi('lito')
   'hi, lito'
   >>> hi()
   'hi, home2'
   >>> 

在上面，我们给了函数 hi 的形参 name 一个默认值 'home2'，当调用函数时没有提供该参数的值，则会使用默认值。

顺便说一下字符串的格式化，上面函数 hi 中的 print 函数还可以写成以下两种形式：

.. code-block:: python

   >>> name = 'lito'
   >>> print('hi, ' + name)
   'hi, lito'
   >>> print('hi, %s' % name)
   'hi, lito'
   >>> print('hi, {}'.format(name))
   'hi, lito'
   >>> 

字符串的格式化可用的选项很丰富，等我们用到的时候再讲解。

我们看看关键字参数，前面我们都是使用位置的方式去传递参数，如：

.. code-block:: python

   >>> def add(a, b):
   ...     print(a + b)
   ... 
   >>> add(3, 4)
   7
   >>> 

在 add(3, 4) 中，我们把 3 传递给了 a，把 4 传递给了 b，这和他们的位置一一对应，但我们其实可以这样调用：

.. code-block:: python

   >>> add(a=4, b=5)
   9
   >>> add(b=10, a=2)
   12
   >>> 

我们可以明确指定传递值给哪个参数。

当关键字参数和默认参数组合在一起，可以提供更灵活的调用方式：

.. code-block:: python

    >>> def greet(name, text='morning', emoji=':)'):
    ...     print('%s, good %s %s' % (name, text, emoji))
    ...
    >>> greet('home2')
    home2, good morning :)
    >>> greet('home2', emoji=';-)')
    home2, good morning ;-)
    >>> greet('lito', emoji=':-)', text='night')
    lito, good night :-)
    >>> 

上面的函数是小鲸鱼打招呼的简化版（emmm 小鲸鱼并不复杂）。

刚才忘了提，没有给定默认值的形参在定义的时候必须放在前面，而在调用的时候也必须提供值给它。

假设你想设计一个函数来计算多个数的和（这只是示例，在 Python 中我们有内置的函数 sum() 可以完成这个工作），那么最初你可能会这样写：

.. code-block:: python

   >>> def mysum(a, b, c):
   ...     return a + b + c
   ... 
   >>> mysum(3, 4, 5)
   12
   >>> 

上面的函数能计算 3 个数的和，它也确实如期工作了，但当想算 4 个数的和呢，这还不简单，在形参中加多一个 d。

但我们有更好的做法，我们可以使用可变参数，让这个函数可以接收任意多个参数：

.. code-block:: python

   >>> def mysum(*num):
   ...     total = 0
   ...     for x in num:
   ...         total += x
   ...     return total
   ...
   >>> mysum(1)
   1
   >>> mysum(1, 2)
   3
   >>> mysum(1, 2, 3)
   6
   >>> mysum(1, 2, 3, 4)
   10
   >>> 

看，新的 mysum 可以接受任意多个参数，并返回它们的和。

请注意到我们在定义新的 mysum 函数时，在形参 num 前面加了星号（\*），这表示 num 可以接受任意多个参数并把值放到一个元组中，于是我们可以在函数体内循环它。

顺便提一下，星号（\*）在传递参数给函数的时候可用于打散列表，看一下代码：

.. code-block:: python

   >>> some = [1, 2, 3, 4, 5]
   >>> mysum(some)
   Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 4, in mysum
   TypeError: unsupported operand type(s) for +=: 'int' and 'list'
   >>> 

当我们尝试把一个包含多个数字的列表传递给 mysum 时，我们得到了一个错误提示，大概意思是不同类型不能用在 += 操作符上，现在神奇的东西来了：

.. code-block:: python

   >>> mysum(*some)
   15
   >>> 

最后来看另一种可变参数：

.. code-block:: python

   >>> def show(name, age, **kw):
   ...     print('name: %s' % name)
   ...     print('age: %s' % age)
   ...     for key, value in kw.items():
   ...         print('%s: %s' % (key, value))
   ...
   >>> show('mr.g', 6)
   name: mr.g
   age: 6
   >>> show('mr.g', 6, gender='man', hobby='greeting')
   name: mr.g
   age: 6
   gender: man
   hobby: greeting
   >>> 

在上面的函数定义中，我们除了有两个普通的形参 name 和 age，还多了一个 \*\*kw。当我们把双星号（\*\*）放一个形参中，它可以接受额外的关键词参数，并收集到一个字典中。和 \* 可打散列表类似，\*\* 可以打散一个字典。

上面提到的各种类型的参数可以同时使用，但出现顺序有所要求：位置参数，默认参数，\*参数，\*\*参数。

关于函数，我们暂时学习到这里，过程中我肯定有不少遗漏，请原谅我。

我们是为了快速学习然后去玩一下饭否 API 写机器人，若在这个过程中你对编程产生了兴趣，在后面我会推荐一些更正式的入门书。

下章我们简单学习一下类和对象，模块和第三方库，以及了解几个常用的饭否 API，就可以开始写机器人啦。
