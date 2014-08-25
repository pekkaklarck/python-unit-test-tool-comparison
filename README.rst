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

``unittest`` compatible tests are in `<test_unittest.py>`__ file and
can be executed easily from the command line::

    $ python test_unittest.py
    F...
    ======================================================================
    FAIL: test_failing (__main__.TestCompare)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_unittest.py", line 21, in test_failing
        self.assertEquals(compare(1, 0), 0)
    AssertionError: 1 != 0

    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    FAILED (failures=1)

The main benefit of ``unittest`` is that being a standard module it is
always available. The main drawback is that it requires writing plenty
of boilerplate code.

nose
----

Also ``nose`` can execute `<test_unittest.py>`__ without problems::

    $ nosetests test_unittest.py
    F...
    ======================================================================
    FAIL: test_failing (test_unittest.TestCompare)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/peke/Devel/python-unit-test-tool-comparison/test_unittest.py", line 21, in test_failing
        self.assertEquals(compare(1, 0), 0)
    AssertionError: 1 != 0

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

``nose`` can also execute `<test_assert.py>`__ which simply uses
``assert`` statement for testing, but it does not provide too good
error message when such tests fail::

    $ nosetests test_assert.py
    ...F
    ======================================================================
    FAIL: test_assert.test_failing
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/dist-packages/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/home/peke/Devel/python-unit-test-tool-comparison/test_unittest.py/test_assert.py", line 17, in test_failing
        assert compare(1, 0) == 0
    AssertionError

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    FAILED (failures=1)

Finally, ``nose`` makes running the whole directory trivial::

    $ nosetests .
    ...FF...
    ======================================================================
    FAIL: test_assert.test_failing
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/dist-packages/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/home/peke/Devel/compare-python-unit-test-tools/test_assert.py", line 17, in test_failing
        assert compare(1, 0) == 0
    AssertionError

    ======================================================================
    FAIL: test_failing (test_unittest.TestCompare)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/peke/Devel/compare-python-unit-test-tools/test_unittest.py", line 21, in test_failing
        self.assertEquals(compare(1, 0), 0)
    AssertionError: 1 != 0

    ----------------------------------------------------------------------
    Ran 8 tests in 0.003s

    FAILED (failures=2)

The main benefit of ``nose`` compared to ``unittest`` is that it has
better test discovery (i.e. functionality run all tests in a
directory, recursively) and that it also supports test with less
boilerplate. Having pretty much identical output as ``unittest`` makes
``nose`` basically a ``ùnittest`` replacement with some extra
features. As already noted above, one problem is that tests with just
``assert`` do not produce any other error message than
``AssertionError``.

py.test
-------

Also ``py.test`` can run ``ùnittest`` based tests::

    $ py.test test_unittest.py
    ======================== test session starts =========================
    platform linux2 -- Python 2.7.3 -- py-1.4.20 -- pytest-2.5.2
    collected 4 items

    test_unittest.py F...

    ============================== FAILURES ==============================
    ______________________ TestCompare.test_failing ______________________

    self = <test_unittest.TestCompare testMethod=test_failing>

        def test_failing(self):
    >       self.assertEquals(compare(1, 0), 0)
    E       AssertionError: 1 != 0

    test_unittest.py:21: AssertionError
    ================= 1 failed, 3 passed in 0.01 seconds =================

``py.test`` supports also ``assert`` based tests and, very nicely,
produces a meaningfull error message also with them::

    $ py.test test_assert.py
    ======================== test session starts =========================
    platform linux2 -- Python 2.7.3 -- py-1.4.20 -- pytest-2.5.2
    collected 4 items

    test_assert.py ...F

    ============================== FAILURES ==============================
    ____________________________ test_failing ____________________________

        def test_failing():
    >       assert compare(1, 0) == 0
    E       assert 1 == 0
    E        +  where 1 = compare(1, 0)

    test_assert.py:17: AssertionError
    ================= 1 failed, 3 passed in 0.01 seconds =================

Finally, also ``py.test`` supports running the whole directory::

    $ py.test .
    ======================== test session starts =========================
    platform linux2 -- Python 2.7.3 -- py-1.4.20 -- pytest-2.5.2
    collected 8 items

    test_assert.py ...F
    test_unittest.py F...

    ============================== FAILURES ==============================
    ____________________________ test_failing ____________________________

        def test_failing():
    >       assert compare(1, 0) == 0
    E       assert 1 == 0
    E        +  where 1 = compare(1, 0)

    test_assert.py:17: AssertionError
    ______________________ TestCompare.test_failing ______________________

    self = <test_unittest.TestCompare testMethod=test_failing>

        def test_failing(self):
    >       self.assertEquals(compare(1, 0), 0)
    E       AssertionError: 1 != 0

    test_unittest.py:21: AssertionError
    ================= 2 failed, 6 passed in 0.03 seconds =================

As already noted above, a very nice ``py.test`` feature is that it
produces a meaningfull error message also with ``assert`` based
tests. Its output may look somewhat strange in the beginning, though,
because it is completely different to the output of ``unittest`` or
other similar ``xUnit`` tools.
