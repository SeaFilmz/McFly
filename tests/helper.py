import os
import sys
sys.path.insert(1, os.getcwd())

from mcfly  import Interpreter, Lexer, Parser, IntNode, FloatNode

def run(subject):
  interpreter = Interpreter()
  lexer = Lexer(subject)
  tokens = list(lexer.generate_tokens())
  parser = Parser(tokens)
  tree = parser.parse()
  return interpreter.visit(tree)

def isNumeric(value):
  return isinstance(value, (IntNode, FloatNode))