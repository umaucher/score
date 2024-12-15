..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Inter-process Communication
###########################

Inter-process Communication (IPC) Framework handles the safe, secure and performant exchange of information between software and/or hardware components of the Score stack.

The IPC framework is independent of the application context it is used in.

There are three fundamental information exchange concepts defined

* **Topics**: A topic is a data entity identifyed by a name, being structured by a *data type* and containing zero to multiple instances of that type (a *value*).
* **Remote Procedures**: A remote procedure is an invocable entity identifyed by a name, being structured by parameters of a *data type* and being activated by an invokation passing arguments, i.e. a value for each parameter.
* **Events**: An event signals the change of the state of something. An event carries no data, only the information "the related state change occurred".

Data Types
----------

Data types describe the inner structure of data entities known as values.

Primitive Types
```````````````

Primitive data types consist of a single element with no further inherent structure.
The following primitive data types and their Rust and C++ representation are defined:

========= ========== ========= ========================== ====== ============================
Data Type Class      Rust      C++                        Size   Description
========= ========== ========= ========================== ====== ============================
Bool      Boolean    ``bool``  ``bool``                   1      A boolean value, true or false
Int8      Integer    ``i8``    ``int8_t``                 1      An 8 bit signed integer
UInt8     Integer    ``u8``    ``uint8_t``                1      An 8 bit unsigned integer
UInt128   Integer    ``u128``  ``uint128_t``              16     An 128 bit unsigned integer
Float16   Floating   ``f16``   ``float16_t``              2      An IEEE 756 32 bit floating point
Float32   Floating   ``f32``   ``float``, ``float32_t``   4      An IEEE 756 32 bit floating point
Float64   Floating   ``f64``   ``double``, ``float64_t``  8      An IEEE 756 64 bit floating point
BFloat16  Floating   ``bf16``  ``bfloat16_t``             2      A Google brain float 16 floating point
Char      String     ``char``  ``char32_t``               4      A unicode codepoint (32 bit)
String    String     ``str``   -                          n/a    A UTF-8 encoded text
========= ========== ========= ========================== ====== ============================

The type ``Byte`` may be used as alias for ``UInt8``.

| Pointers are no recognized primitive types.
| References are no recognized primitive types.

Tuples
``````

Tuples are ordered collections of arbitrary data types. A tuple shall be expressed by parentheses:
``(Int8, Float32)``.

Structs
```````

A struct is an ordered collection of named arbitrary data types called fields:

::

   struct MyStruct {
      field1: Int8,
      field2: Float32
   }

Arrays
``````

Arrays are ordered collections of data elements of the same type with a fixed length. A single element is addressed by an *index*:

::

   Char[32]


Tensors
```````

A Tensor is a multi-dimensional array of numerical values that generalizes scalars, vectors, and matrices to higher dimensions, commonly used in mathematics, physics, and machine learning.

The number of dimensions is called the *rank* or *order* of the Tensor.
The vector of dimensions with the Tensor's rank is called the *shape* of the Tensor.

::

   Tensor<Float16, [5, 5, 128]>

The 5x5 kernel of a CNN layer with 128 features.

List
````

A List is an ordered collection of data elements of the same type with a variable length. A single element is addressed by an *index*:

::

   List<Char>

HashMap
```````

A HashMap is an unordered collection of data element of the same type with variable length. A single element is addressed by a *key* of a specific data type.

::

   HashMap<UInt32, String>


Topic Reference
```````````````

A topic reference is a data type that provides a resolvable reference to a Topic.

::

   TopicRef

The underlying implementation shall not use more than 64 bits for the representation of TopicRef.

All properties of the referenced topics shall be retrievable through the TopicRef.

Data access to the content of the Topic shall be possible through the TopicRef.


RP Reference
`````````````

An RP Reference is a data type that provides a resolvable reference to a Remote Procedure.

::

   RPRef

The underlying implementation shall not use more than 64 bits for the representation of RPRef.

All properties of the referenced Remote Procedure shall be retrievable through the RPRef.

Invocation of the referenced Remote Procedure shall be possible through the RPRef.


Namespaces
----------


Topics
------

* Name
* Data Type
* Queue Depth
* Initialization
* Publisher
* Subscriber


Remote Procedures
-----------------

* Name
* Signature, Parameter Pack
* Publishing
* Discovery
* Invocation
* Sync/Async

Events
------

* Name
* Publisher
* Subscriber
* Chains / Buffering


Zero Copy
---------

* Definition
* Shared Memory
* Memory Management
* DMA


Safety
------
