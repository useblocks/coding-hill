C questions
===========

.. qu:: When should we use pointers in a C program?
   :id: c_1
   :tags: c

.. qu:: What is NULL pointer?
   :id: c_2
   :tags: c

.. qu:: What are local static variables? What is their use?
   :id: c_3
   :tags: c

.. qu:: What are static functions? What is their use?
   :id: c_4
   :tags: c

.. qu:: What are the basic data types associated with C?
   :id: c_5
   :tags: c

.. qu:: What is the difference between \+\+a and a\+\+?
   :id: c_6
   :tags: c

.. qu:: What is the explanation for prototype function in C?
   :id: c_7
   :tags: c

.. qu:: Describe the header file and its usage in C programming?
   :id: c_8
   :tags: c

.. qu:: Convert the decimal number 35 to binary.
   :id: c_9
   :tags: c

.. qu:: Advanced C programming - pointers, qualifiers, MISRA, coding
    :id: c_10
    :tags: c

    .. code-block:: c

        /*  Tasks:
         *  - What are #pragma commands good for?
         *  - Why is 'const volatile' used?
         *  - What is MISRA-C?
         *  - Finish function kl_ipol_u16_u16 so that the 3rd element of the input array xTab is returned.
         */

        #pragma section D_U16_KL

        const volatile uint16 AXX_D[5] = { 10, 20, 30, 40, 50};

        #pragma section

        (...)

        #pragma section C_10MS

        uint16 kl_ipol_u16_u16(const volatile void *xTab, u16 x) {

            /* automatic variable */
            uint16 yy;



            /* MISRA-C conform access to element 3 of xTab (type uint16) */
            yy =





            return yy;
        }

        #pragma section

        void another_function(void) {

            /* Example call */
            uint16 result ;
            result = kl_ipol_u16_u16(AXX_D, 42);

        }

.. qu:: What's the difference between compiler and linker?
    :id: c_11
    :tags: c
