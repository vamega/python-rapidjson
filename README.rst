python-rapidjson
================
python-rapidjson is a fast, simple JSON serialization library based on the
wonderful RapidJSON_ C++ library.  python-rapidjson shares many features with
the standard library ``json`` module so that you can use it as a drop-in
replacement.

We do not support legacy python versions, you will need to upgrade to Python 3
to use this library.

Goal (Why another JSON library?)
--------------------------------
python-rapidjson tries to balance performance and compatibility with the
standard library ``json`` module.  Performance is the main goal, but
compatibility with the standard library is added where practical and if
performance is not worsened too much.

python-rapidjson was created because we were not aware of a library that tries
to balance performance and compatibility.

Getting Started
---------------
First install ``python-rapidjson``:

.. code-block:: bash

    $ pip install python-rapidjson

Basic usage:

.. code-block:: python

    >>> import rapidjson
    >>> data = {'foo': 100, 'bar': 'baz'}
    >>> rapidjson.dumps(data)
    '{"bar":"baz","foo":100}'
    >>> rapidjson.loads('{"bar":"baz","foo":100}')
    {'bar': 'baz', 'foo': 100}


Performance
-----------
python-rapidjson is fast because RapidJSON_ is fast.  Here are our current benchmarks:

+-----------------------------------------+--------+------------+------------+-----------+
|                                         | ujson  | simplejson | rapidjson  | yajl      |
+=========================================+========+============+============+===========+
| Array with 256 doubles                  |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+
| Encode                                  | 13.81s | 12.58s     | 1.82s      | 8.36s     |
+-----------------------------------------+--------+------------+------------+-----------+
| Decode                                  | 2.00s  | 4.65s      | 2.19s      | 2.09s     |
+-----------------------------------------+--------+------------+------------+-----------+
|                                         |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+
| Array with 256 utf-8 strings            |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+
| Encode                                  | 1.98s  | 2.36s      | 5.09s      | 1.45s     |
+-----------------------------------------+--------+------------+------------+-----------+
| Decode                                  | 2.77s  | 13.58s     | 2.42s      | 7.19s     |
+-----------------------------------------+--------+------------+------------+-----------+
|                                         |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+
| 100 dictionaries of 100 arrays          |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+
| Encode                                  | 1.65s  | 5.20s      | 0.77s      | 2.09s     |
+-----------------------------------------+--------+------------+------------+-----------+
| Decode                                  | 2.76s  | 3.86s      | 2.79s      | 3.47      |
+-----------------------------------------+--------+------------+------------+-----------+
|                                         |        |            |            |           |
+-----------------------------------------+--------+------------+------------+-----------+

To run these tests yourself, clone the repo and run:

.. code-block:: bash

   $ tox -e py34 -m benchmark

As with any benchmarks, the only useful benchmarks are the ones you gather for
your specific use case.


Incompatibility with ``json``
-----------------------------
Here are things the standard library ``json`` module supports that we have decided
not to support:

* ``separators`` argument. This is mostly used for pretty printing and not
  supported by RapidJSON, so it isn't a high priority. We do support the
  ``indent`` kwarg that would get you nice looking JSON anyways.

* Coercing keys when dumping. ``json`` will turn ``True`` into ``'True'`` if you
  dump it out but when you load it back in it'll still be a string. We want the
  dump and load to return the exact same objects so we have decided not to do
  this coercing.


Why RapidJSON?
--------------

changes to rapidjson
--------------------

design decisions
----------------

.. _RapidJSON: https://github.com/miloyip/rapidjson
