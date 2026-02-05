import os
import sys
import unittest

from helper import *;

sys.path.insert(1, os.getcwd())


from mcfly  import Interpreter, Lexer, Parser, IntNode, FloatNode

class TestOperation(unittest.TestCase):

  def test_add(self):
    result = run("4 + 4");
    self.assertEqual(result, 8)

  def test_subtract(self):
    result = run("4 - 4");
    self.assertEqual(result, 0)

  def test_multiply(self):
    result = run("4 * 4");
    self.assertEqual(result, 16)

  def test_divide(self):
    result = run("4 / 4");
    self.assertEqual(result, 1)

  def test_negate(self):
    result = run("-100");
    self.assertEqual(result, -100)

  def test_positive(self):
    result = run("+100");
    self.assertEqual(result, 100)

  def test_recursive_add(self):
    result = run("4 + mean(4,4)");
    self.assertEqual(result, 8)

  def test_recursive_add2(self):
    result = run("4 + mean(4,4) + mean(3 + 1, 3 + 1)");
    self.assertEqual(result, 12)

  def test_recursive_subtract(self):
    result = run("4 - mean(4,4)");
    self.assertEqual(result, 0)

  def test_recursive_subtract(self):
    result = run("4 - mean(4,4) - mean(3 + 1, 3 + 1)");
    self.assertEqual(result, -4)

  def test_recursive_multiply(self):
    result = run("4 * mean(4,4)");
    self.assertEqual(result, 16)

  def test_recursive_multiply2(self):
    result = run("mean(4,4) * mean(4,4)");
    self.assertEqual(result, 16)

  def test_recursive_divide(self):
    result = run("4 / mean(4,4)");
    self.assertEqual(result, 1)

  def test_recursive_divide2(self):
    result = run("mean(4,4) / mean(4,4)");
    self.assertEqual(result, 1)

  def test_recursive_negate(self):
    result = run("-mean(100,100)");
    self.assertEqual(result, -100)

  def test_recursive_positive(self):
    result = run("+mean(100,100)");
    self.assertEqual(result, 100)