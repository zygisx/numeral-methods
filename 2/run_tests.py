#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.test_suite import Task_2_TestSuite

def main():
    task1 = Task_1_TestSuite()
    runner = unittest.TextTestRunner()
    result = runner.run(task1.suite())
    exit_code = 0 if result.wasSuccessful() else -1
    sys.exit(exit_code)

if __name__ == '__main__':
    main()