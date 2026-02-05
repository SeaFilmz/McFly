import os
import sys
import unittest

from helper import *;

sys.path.insert(1, os.getcwd())


from mcfly  import Interpreter, Lexer, Parser, IntNode, FloatNode


class TestMean(unittest.TestCase):

  def test_mean(self):
    result = run("mean(4,4)");
    self.assertTrue(result, isNumeric(result))
    self.assertEqual(result.value, 4)
  
  def test_recursive_mean(self):
    result = run("mean(mean(4,4),mean(4,4))");
    self.assertEqual(result.value, 4)

  def test_recursive_mean2(self):
    result = run("mean(4,4,4,mean(4,4), 4, 4)");
    self.assertEqual(result.value, 4)
