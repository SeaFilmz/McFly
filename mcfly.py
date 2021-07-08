from enum import Enum
import string
from dataclasses import dataclass, field

# Important Characters #

WHITESPACE = ' \n\t'
DIGITS  = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS_US = LETTERS + DIGITS + '_'

# Dictionary #

important_numbers = {
  '#pi': 3.14159265,
  '#e': 2.71828182
}

important_words = {
  'fun': 'Coming Soon: The word fun is reserved for creating functions.',
  'if': 'Coming Soon: The word if is reserved for conditionals.',
  'sum': 'Cooming Soon: The word sum is reserved for adding all the numbers in a set together.',
  'avg': 'Cooming Soon: The term avg is reserved for calculating the average of a set numbers.'
}

error_words = {
  'and': 'Error: Code can not start with the word and.',
  'or': 'Error: Code can not start with the word or.',
  'not': 'Error: Code can not start with the word not.'
}

# Tokens #

class TokenType(Enum):
  INTEGER        = 0
  FLOAT          = 1
  PLUS           = 2
  MINUS          = 3
  MULTIPLY       = 4
  DIVIDE         = 5
  LPAREN         = 6
  RPAREN         = 7
  NUMBER_VAR     = 8
  STRING_VAR     = 9
  ARRAY_VAR      = 10
  EQUAL          = 11
  GT             = 12
  LT             = 13
  STRING         = 14

# Lexer #

class Lexer:
  def __init__(self, text):
    self.text = iter(text)
    self.advance()

  def advance(self):
    try:
      self.current_char = next(self.text)
    except StopIteration:
      self.current_char = None

  def generate_tokens(self):
    while self.current_char != None:
      if self.current_char in WHITESPACE:
        self.advance()
      elif self.current_char in DIGITS:
        yield self.generate_number()
      elif self.current_char == '#':
        yield self.generate_num_var()
      elif self.current_char == '$':
        yield self.generate_str_var()
      elif self.current_char == '@':
        yield self.generate_array_var()
      elif self.current_char in LETTERS:
        yield self.generate_string()
      elif self.current_char == '+':
        self.advance()
        yield Token(TokenType.PLUS)
      elif self.current_char == '-':
        self.advance()
        yield Token(TokenType.MINUS)
      elif self.current_char == '*':
        self.advance()
        yield Token(TokenType.MULTIPLY)
      elif self.current_char == '/':
        self.advance()
        yield Token(TokenType.DIVIDE)
      elif self.current_char == '(':
        self.advance()
        yield Token(TokenType.LPAREN)
      elif self.current_char == ')':
        self.advance()
        yield Token(TokenType.RPAREN)
      elif self.current_char == '=':
        self.advance()
        yield Token(TokenType.EQUAL)
      elif self.current_char == '>':
        self.advance()
        yield Token(TokenType.GT)
      elif self.current_char == '<':
        self.advance()
        yield Token(TokenType.LT)
      else:
        raise Exception(f"llegal Character '{self.current_char}'")

  def generate_number(self):
    decimal_point_count = 0
    number_str = self.current_char
    self.advance() 

    while self.current_char != None and (self.current_char in DIGITS + '.'):
      if self.current_char == '.': 
        decimal_point_count += 1
        if decimal_point_count > 1:
          break

      number_str += self.current_char
      self.advance()

    if number_str.endswith('.'):
      number_str += '0'

    if decimal_point_count == 0:
      return Token(TokenType.INTEGER, int(number_str))
    else:
      return Token(TokenType.FLOAT, float(number_str))

  def generate_string(self):
    string_str = self.current_char
    self.advance()

    while self.current_char != None:

      string_str += self.current_char
      self.advance()

    return Token(TokenType.STRING, str(string_str))

  def generate_num_var(self):
    num_sign_var = self.current_char
    self.advance()

    while self.current_char != None and self.current_char in LETTERS_DIGITS_US:
      num_sign_var += self.current_char
      self.advance()

    return Token(TokenType.NUMBER_VAR, num_sign_var)

  def generate_str_var(self):
    str_sign_var = self.current_char
    self.advance()

    while self.current_char != None and self.current_char in LETTERS_DIGITS_US:
      str_sign_var += self.current_char
      self.advance()

    return Token(TokenType.STRING_VAR, str_sign_var)

  def generate_array_var(self):
    array_sign_var = self.current_char
    self.advance()

    while self.current_char != None and self.current_char in LETTERS_DIGITS_US:
      array_sign_var += self.current_char
      self.advance()

    return Token(TokenType.ARRAY_VAR, array_sign_var)

# Nodes #

@dataclass
class Token:
  type: TokenType
  value: any = None

  def __repr__(self):
    return self.type.name + ((f":{self.value}") if self.value != None else "")

@dataclass
class IntNode:
  value: int

  def __repr__(self):
    return f"{self.value:d}"

@dataclass
class FloatNode:
  value: float

  def __repr__(self):
    return f"{self.value}"

@dataclass
class StringNode:
  value: str
  WordFun = important_words['fun']
  WordIf = important_words['if']  
  ErrorAnd = error_words['and']
  ErrorOr = error_words['or']
  ErrorNot = error_words['not']
  WordSum = important_words['sum']
  WordAvg = important_words['avg']

  def __repr__(self):
    return f"{self.value}"

@dataclass
class AddNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"({self.node_a}/{self.node_b})"

@dataclass
class PlusNode:
  node: any

  def __repr__(self):
    return f"(+{self.node})"

@dataclass
class MinusNode:
  node: any

  def __repr__(self):
    return f"(-{self.node})"

@dataclass
class NumberSignNode:
  value: str
  StartValuePi = important_numbers['#pi']
  StartValueE = important_numbers['#e']

  def __repr__(self):
    return f"{self.value}"

@dataclass
class StringSignNode:
  value: str

  def __repr__(self):
    return f"{self.value}"

@dataclass
class ArraySignNode:
  value: str

  def __repr__(self):
    return f"{self.value}"

@dataclass
class EqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}={self.node_y})"

@dataclass
class GreaterThanNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}>{self.node_y})"

@dataclass
class LessThanNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}<{self.node_y})"

# Parser #

class Parser:
  def __init__(self, tokens):
    self.tokens = iter(tokens)
    self.advance()

  def raise_error(self):
    raise Exception("Invalid Syntax")

  def advance(self):
    try:
      self.current_token = next(self.tokens)
    except StopIteration:
      self.current_token = None

  def parse(self):
    if self.current_token == None:
      return None

    result = self.expr()

    if self.current_token != None:
      self.raise_error()

    return result

  def expr(self):
    result = self.term()

    while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
      if self.current_token.type == TokenType.PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif self.current_token.type == TokenType.MINUS:
        self.advance()
        result = SubtractNode(result, self.term())

    return result

  def term(self):
    result = self.equalCheck()

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.equalCheck())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.equalCheck())

    return result

  def equalCheck(self):
    result = self.greaterCheck()

    while self.current_token != None and self.current_token.type in (TokenType.EQUAL, TokenType.EQUAL):
      if self.current_token.type == TokenType.EQUAL:
        self.advance()
        result = EqualNode(result, self.greaterCheck())
      elif self.current_token.type == TokenType.EQUAL:
        self.advance()
        result = EqualNode(result, self.greaterCheck())

    return result


  def greaterCheck(self):
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.GT, TokenType.GT):
      if self.current_token.type == TokenType.GT:
        self.advance()
        result = GreaterThanNode(result, self.factor())
      elif self.current_token.type == TokenType.GT:
        self.advance()
        result = GreaterThanNode(result, self.factor())

    return result


  def factor(self):
    token = self.current_token

    if token.type == TokenType.LPAREN:
      self.advance()
      result = self.expr()

      if self.current_token.type != TokenType.RPAREN:
        self.raise_error()
      
      self.advance()
      return result
    elif token.type == TokenType.INTEGER:
      self.advance()
      return IntNode(token.value)
    elif token.type == TokenType.FLOAT:
      self.advance()
      return FloatNode(token.value)
    elif token.type == TokenType.PLUS:
      self.advance()
      return PlusNode(self.factor())
    elif token.type == TokenType.MINUS:
      self.advance()
      return MinusNode(self.factor())
    elif token.type == TokenType.STRING:
      self.advance()
      return StringNode(token.value)
    elif token.type == TokenType.NUMBER_VAR:
      self.advance()
      return NumberSignNode(token.value)
    elif token.type == TokenType.STRING_VAR:
      self.advance()
      return StringSignNode(token.value)
    elif token.type == TokenType.ARRAY_VAR:
      self.advance()
      return ArraySignNode(token.value)
    self.raise_error()

# Interpreter #

class Interpreter:
  def visit(self, node):
    method_name = f'visit_{type(node).__name__}'
    method = getattr(self, method_name)
    return method(node)

  def visit_IntNode(self, node):
    if (isinstance(node.value, int)):
      return IntNode(node.value)

  def visit_FloatNode(self, node):
    if (isinstance(node.value, float)):
      return FloatNode(node.value)

  def visit_NumberSignNode(self, node):
    if node.value == '#pi':
      return NumberSignNode(node.StartValuePi)
    elif node.value == '#e':
      return NumberSignNode(node.StartValueE)
    else:
      return NumberSignNode(node.value)

  def visit_StringSignNode(self, node):
    return StringSignNode(node.value)

  def visit_ArraySignNode(self, node):
    return ArraySignNode(node.value)

  def visit_StringNode(self, node):
    if node.value == 'fun':
      return StringNode(node.WordFun)
    elif node.value == 'if':
      return StringNode(node.WordIf)    
    elif node.value == 'and':
      return StringNode(node.ErrorAnd)
    elif node.value == 'or':
      return StringNode(node.ErrorOr)
    elif node.value == 'not':
      return StringNode(node.ErrorNot)
    elif node.value == 'sum':
      return StringNode(node.WordSum)
    elif node.value == 'avg':
      return StringNode(node.WordAvg)             
    else:
      return StringNode(node.value)

  def visit_EqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if isinstance(check_x, int) and isinstance(check_y, float):    
      return 'False'
    elif isinstance(check_x, float) and isinstance(check_y, int):    
      return 'False'
    elif isinstance(check_x, int) and isinstance(check_y, int):
      if int(check_x) == int(check_y):
        return 'True'
      elif int(check_x) != int(check_y):
        return 'False'
    elif isinstance(check_x, float) and isinstance(check_y, float):
      if float(check_x) == float(check_y):
        return 'True'
      elif float(check_x) != float(check_y):
        return 'False'

  def visit_GreaterThanNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if isinstance(check_x, int) and isinstance(check_y, int):
      if int(check_x) > int(check_y):
        return 'True'
      elif int(check_x) < int(check_y):
        return 'False'
      elif int(check_x) == int(check_y):
        return 'False'
    elif isinstance(check_x, float) and isinstance(check_y, float):
      if float(check_x) > float(check_y):
        return 'True'
      elif float(check_x) < float(check_y):
        return 'False'
      elif float(check_x) == float(check_y):
        return 'False'
    elif isinstance(check_x, int) and isinstance(check_y, float):
      if int(check_x) > float(check_y):
        return 'True'
      elif int(check_x) < float(check_y):
        return 'False'
      elif int(check_x) == float(check_y):
        return 'False'
    elif isinstance(check_x, float) and isinstance(check_y, int):
      if float(check_x) > int(check_y):
        return 'True'
      elif float(check_x) < int(check_y):
        return 'False'
      elif float(check_x) == int(check_y):
        return 'False'

  def visit_AddNode(self, node):
    check_num_a = self.visit(node.node_a).value
    check_num_b = self.visit(node.node_b).value

    if isinstance(check_num_a, int) and isinstance(check_num_b, int):
      return IntNode(check_num_a + check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
      return FloatNode(check_num_a + check_num_b)
    elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
      return FloatNode(check_num_a + check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
      return FloatNode(check_num_a + check_num_b)

  def visit_SubtractNode(self, node):
    check_num_a = self.visit(node.node_a).value
    check_num_b = self.visit(node.node_b).value

    if isinstance(check_num_a, int) and isinstance(check_num_b, int):
      return IntNode(check_num_a - check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
      return FloatNode(check_num_a - check_num_b)
    elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
      return FloatNode(check_num_a - check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
      return FloatNode(check_num_a - check_num_b)

  def visit_MultiplyNode(self, node):
    check_num_a = self.visit(node.node_a).value
    check_num_b = self.visit(node.node_b).value

    if isinstance(check_num_a, int) and isinstance(check_num_b, int):
      return IntNode(check_num_a * check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
      return FloatNode(check_num_a * check_num_b)
    elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
      return FloatNode(check_num_a * check_num_b)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
      return FloatNode(check_num_a * check_num_b)

  def visit_DivideNode(self, node):
    try:
      check_num_a = self.visit(node.node_a).value
      check_num_b = self.visit(node.node_b).value
    
      if isinstance(check_num_a, int) and isinstance(check_num_b, int):
        return IntNode(check_num_a / check_num_b)
      elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
        return FloatNode(check_num_a / check_num_b)
      elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
        return FloatNode(check_num_a / check_num_b)
      elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
        return FloatNode  (check_num_a / check_num_b)
    except:
      raise Exception("Runtime math error")
  
  def visit_PlusNode(self, node):
    return self.visit(node.node)
  
  def visit_MinusNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
      return IntNode(-check_num)  
    elif isinstance(check_num, float):
      return FloatNode(-check_num)

# Run #

while True:
  text = input("Enter a math function: ")
  lexer = Lexer(text)
  tokens = lexer.generate_tokens()
  parser = Parser(tokens)
  tree = parser.parse()
  if not tree: continue
  interpreter = Interpreter()
  value = interpreter.visit(tree)
  print(tree)
  print(value)