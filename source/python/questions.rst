Python questions
================

.. needlist::
   :tags: python
   :types: qu


.. qu:: What is Python really?
   :id: python_1
   :tags: python

   You can (and are encouraged) make comparisons to other technologies in your answer


.. qu:: What are the final values of following vars?
   :id: python_2
   :tags: python

   .. code-block:: python

      A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
      A1 = range(10)
      A2 = sorted([i for i in A1 if i in A0])
      A3 = sorted([A0[s] for s in A0])
      A4 = [i for i in A1 if i in A3]
      A5 = {i:i*i for i in A1}
      A6 = [[i,i*i] for i in A1]

      zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

      Return a list of tuples, where each tuple contains the i-th element
      from each of the argument sequences.  The returned list is truncated
      in length to the length of the shortest argument sequence.


.. qu:: Python and multi-threading.
   :id: python_3
   :tags: python

   Is it a good idea? List some ways to get some Python code to run in a parallel way.


.. qu:: Loops and parameters
   :id: python_4
   :tags: python

   What does this code output?

   .. code-block:: python

      def f(x,l=[]):
          for i in range(x):
              l.append(i*i)
          print(l)

      f(2)
      f(3,[3,2,1])
      f(3)

   Answer: https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6#answer

.. qu:: What is monkey patching and is it ever a good idea?
   :id: python_5
   :tags: python

.. qu:: What does this stuff mean: \*args, \*\*kwargs? And why would we use it?
   :id: python_6
   :tags: python

.. qu:: For what is @property good for?
   :id: python_7
   :tags: python

.. qu:: What are decorators?
   :id: python_8
   :tags: python

.. qu:: Which tools are using a ``setup.py`` file?
   :id: python_9
   :tags: python

.. qu:: Who is the inventor of Python and what is his/her official title?
   :id: python_10
   :tags: python

.. qu:: Class inheritance: What is the output?
   :id: python_11
   :tags: python

   .. literalinclude:: python_11.py

