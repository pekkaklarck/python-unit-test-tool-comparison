Comparing Python unit testing tools
===================================

This repository contains very simple examples that allow comparing
Python standard unittest__ module with nose__ and `py.test`__ unit
testing tools in practice. This is not intended to be a full scape
comparison of these tools, though.

__ https://docs.python.org/2/library/unittest.html
__ https://nose.readthedocs.org
__ http://pytest.org

unittest
--------

``unittest`` compatible tests are in `<test_unittest.py>`__ file. It
can be executed simply using::

    python test_unittest.py

The main benefit of ``unittest`` is that being a standard module it is
always available. The main drawback is that it requires writing plenty
of boilerplate code.

nose
----

Also ``nose`` can execute `<test_unittest.py>`__ without problems::

    nosetests test_unittest.py

Additionally it can execute `<test_assert.py>`__ which simply uses
``assert`` statement for testing. It also makes it trivial to run the
whole directory::

    nosetests test_assert.py
    nosetests .

The main benefit of ``nose`` compared to ``unittest`` is that it has
better test discovery (i.e. functionality run all tests in a
directory, recursively) and that it also supports test with less
boilerplate. Having pretty much identical output as ``unitteest``
makes ``nose`` basically a ``ùnittest`` replacement with some extra
features. One problem is that test with just ``assert`` do not produce
any other error message than ``AssertionError``.

py.test
-------

Also ``py.test`` can run both ``ùnittest`` and ``assert`` based tests and
also supports running the whole directory::

    py.test test_unittest.py
    py.test test_assert.py
    py.test .

A very nice ``py.test`` feature is that it produces a meaningfull
error message also with ``assert`` based tests::

        def test_failing():
    >       assert compare(1, 0) == 0
    E       assert 1 == 0
    E        +  where 1 = compare(1, 0)

    test_assert.py:17: AssertionError

``py.test`` output may look somewhat strange in the beginning because
it is completely different to output of ``unittest`` or other similar
``xUnit`` tools.
