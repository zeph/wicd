def run_tests():
    import unittest
    test_suite = unittest.TestSuite()

    from . import testwnettools
    test_suite.addTest(testwnettools.suite())

    from . import testmisc
    test_suite.addTest(testmisc.suite())

    unittest.TextTestRunner(verbosity=2).run(test_suite)
