Python answers
==============

.. needlist::
   :tags: python
   :types: an

.. an:: What is Python really?
   :tags: python
   :links: python_1

   Answer: https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6#answer

   Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.

   Python is dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error

   Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++'s public, private), the justification for this point is given as "we are all adults here"

   In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects

   Writing Python code is quick but running it is often slower than compiled languages. Fortunately， Python allows the inclusion of C based extensions so bottlenecks can be optimised away and often are. The numpy package is a good example of this, it's really quite quick because a lot of the number crunching it does isn't actually done by Python

   Python finds use in many spheres - web applications, automation, scientific modelling, big data applications and many more. It's also often used as "glue" code to get other languages and components to play nice.

   Python makes difficult things easy so programmers can focus on overriding algorithms and structures rather than nitty-gritty low level details.


.. an:: What are the final values of following vars?
   :tags: python
   :links: python_2

   .. code-block:: python

      0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}  # the order may vary
      A1 = range(0, 10) # or [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in python 2
      A2 = []
      A3 = [1, 2, 3, 4, 5]
      A4 = [1, 2, 3, 4, 5]
      A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
      A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

   Answer: https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6#question-3

.. an:: Python and multi-threading.
   :tags: python
   :links: python_3

   Python doesn't allow multi-threading in the truest sense of the word. It has a multi-threading package but if you want to multi-thread to speed your code up, then it's usually not a good idea to use it. Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core. All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package often isn't a good idea.

   There are reasons to use Python's threading package. If you want to run some things simultaneously, and efficiency is not a concern, then it's totally fine and convenient. Or if you are running code that needs to wait for something (like some IO) then it could make a lot of sense. But the threading library won't let you use extra CPU cores.

   Multi-threading can be outsourced to the operating system (by doing multi-processing), some external application that calls your Python code (eg, Spark or Hadoop), or some code that your Python code calls (eg: you could have your Python code call a C function that does the expensive multi-threaded stuff).

.. an:: Loops and parameters
   :tags: python
   :links: python_4

   .. code-block:: python

      [0, 1]
      [3, 2, 1, 0, 1, 4]
      [0, 1, 0, 1, 4]

   The first function call should be fairly obvious, the loop appends 0 and then 1 to the empty list, l. l is a name for a variable that points to a list stored in memory.
   The second call starts off by creating a new list in a new block of memory. l then refers to this new list. It then appends 0, 1 and 4 to this new list. So that's great.
   The third function call is the weird one. It uses the original list stored in the original memory block. That is why it starts off with 0 and 1.

   Answer: https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6#answer-6

.. an:: What is monkey patching and is it ever a good idea?
   :tags: python
   :links: python_5

   Monkey patching is changing the behaviour of a function or object after it has already been defined. For example::

      import datetime
      datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)

   Most of the time it's a pretty terrible idea - it is usually best if things act in a well-defined way. One reason to monkey patch would be in testing. The mock package is very useful to this end.

.. an:: What does this stuff mean: \*args, \*\*kwargs? And why would we use it?
   :tags: python
   :links: python_6

   Use \*args when we aren't sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. \*\*kwargs is used when we dont know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use \*bob and \*\*billy but that would not be wise.

.. an:: For what is @property good for?
   :tags: python
   :links: python_7

   It makes a class method to be accessible as class parameters and behave like this.
   So ``jira.open_issues`` could simply return a number, but in the background the jira server get ask every time this
   "variable" is used.

.. an:: Who is the inventor of Python and what is his/her official title?
   :tags: pyhton
   :links: python_10

   Guido van Rossum - Benevolent dictator of life

.. an:: Class inheritance: What is the output?
   :tags: python
   :links: python_11

   .. code-block:: python

      D()

      C
      A
      B
      D

   Before super() calls functions from the above level, it checks if on the current level "siblings" exists and calls them.

   .. code-block:: text

        A
       /
      B   C
       \ /
        D

