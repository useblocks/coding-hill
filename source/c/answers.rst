C answers
=========

.. an:: When should we use pointers in a C program?
   :links: c_1
   :tags: c

   #. To get address of a variable
   #. For achieving pass by reference in C: Pointers allow different functions to share and modify their local variables.
   #. To pass large structures so that complete copy of the structure can be avoided.
   #. To implement “linked” data structures like linked lists and binary trees.

.. an:: What is NULL pointer?
   :links: c_2
   :tags: c

   NULL is used to indicate that the pointer doesn’t point to a valid location. Ideally, we should initialize pointers as NULL if we don’t know their value at the time of declaration. Also, we should make a pointer NULL when memory pointed by it is deallocated in the middle of a program.


.. an:: What are local static variables? What is their use?
   :links: c_3
   :tags: c

   A local static variable is a variable whose lifetime doesn’t end with a function call where it is declared. It extends for the lifetime of complete program. All calls to the function share the same copy of local static variables. Static variables can be used to count the number of times a function is called. Also, static variables get the default value as 0. For example, the following program prints “0 1”

   .. code-block:: c

      #include <stdio.h>
      void fun()
      {
          // static variables get the default value as 0.
          static int x;
          printf("%d ", x);
          x = x + 1;
      }

      int main()
      {
          fun();
          fun();
          return 0;
      }
      // Output: 0 1


.. an:: What are static functions? What is their use?
   :links: c_4
   :tags: c

   In C, functions are global by default. The “static” keyword before a function name makes it static. Unlike global functions in C, access to static functions is restricted to the file where they are declared. Therefore, when we want to restrict access to functions, we make them static. Another reason for making functions static can be reuse of the same function name in other files.


.. an:: What are the basic data types associated with C?
   :links: c_5
   :tags: c

    * Int – Represent number (integer)
    * Float – Number with a fraction part
    * Double – Double-precision floating point value
    * Char – Single character
    * Void – Special purpose type without any value


.. an:: What is the difference between \+\+a and a\+\+ ?
   :links: c_6
   :tags: c

   ``++a``  is called prefixed increment and the increment will happen first on a variable. ``a++`` is called postfix increment and the increment happens after the value of a variable used for the operations.


.. an:: What is the explanation for prototype function in C?
   :links: c_7
   :tags: c

   * Name of the function.
   * The return type of the function.
   * Parameters list of the function.
   
   ``int Sum(int, int);``


.. an:: Describe the header file and its usage in C programming?
   :links: c_8
   :tags: c

   The file contains the definitions and prototypes of the functions being used in the program are called a header file. It is also known as a library file.


.. an:: Convert the decimal number 35 to binary.
    :links: c_9
    :tags: c

    decimal 35 == 0b100011 == 0x23

    1*2^0 + 1*2^1 + 1*2^5 = 1 + 2 + 32

.. an:: Advanced C programming - pointers, qualifiers, MISRA, coding
    :links: c_10
    :tags: c

    *   #pragma is for compiler directives that are machine-specific or operating-system-specific,
        i.e. it tells the compiler to do something, set some option, take some action, override some default,
        etc. that may or may not apply to all machines and operating systems.

        In this case the compiler is told to put the next code/variable into a specific memory section.

    *   The vector is constant which means the C code must not contain a command that changes the values of
        AXX_D. This would lead to a compiler error.

    *   volatile tells the compiler that the value of AXX_D may change outside the current scope.
        In this case the variable is global and the values of AXX_D may be changed during runtime by the application
        system. Without volatile, the compiler is allowed to optimize the code and put the variable e.g. into a
        register. So the variable may not be read anymore from the original location and changes to that location are
        not recognized.

    *   MISRA-C is a C programming standard in the automotive industry which was designed by the MISRA
        (Motor Industry Software Reliability Association). The first MISRA standard was desdigned for C in 1998.
        MISRA defines over 100 rules for safe programming. Goal is to avoid runtime errors introduced by unsafe C
        constructs. Structural weaknesses lead to misunderstands between developers which should be avoided.

    *   .. code:: C

            /* cast the void pointer to a pointer of type uint16 */
            uint16 *ptrX = (uint16 *)xTab;

            /* MISRA-C compliant access to the elements of xTab (uint16) */
            yy = ptrX[2];

.. an:: What's the difference between compiler and linker?
    :links: c_11
    :tags: c

    The compiler converts code written in a human-readable programming language into a machine code representation
    which is understood by your processor. This step creates object files.

    Once this step is done by the compiler, another step is needed to create a working executable that can be invoked
    and run, that is, associate the function calls (for example) that your compiled code needs to invoke in order
    to work.
    For example, your code could call sprintf, which is a routine in the C standard library.
    Your code has nothing that does the actual service provided by sprintf, it just reports that it must be called,
    but the actual code resides somewhere in the common C library.
    To perform this (and many others) linkages, the linker must be invoked.
    After linking, you obtain the actual executable that can run.
