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
  STRING         = 12

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
        yield self.make_equal()
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

  def make_equal(self):
    equal_sign_count = 0
    equal_sign = self.current_char
    self.advance()

    while self.current_char != None:
      if self.current_char == '=': 
        equal_sign_count += 1
        if equal_sign_count > 1:
          break

      equal_sign += self.current_char
      self.advance()

    if equal_sign.startswith('='):
      print('Error: You Can Not Start a Program with an =')

    return Token(TokenType.EQUAL, str(equal_sign))

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
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.factor())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.factor())

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
    elif token.type == TokenType.EQUAL:
      self.advance()
      return EqualNode(token.node_y)
        
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
    return StringNode(node.value)

  def visit_EqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if check_x and check_y:
      return EqualNode(check_y)

  def visit_AddNode(self, node):
    check_num_a = self.visit(node.node_a).value
    check_num_b = self.visit(node.node_b).value

    if (isinstance(check_num_a, int) and isinstance(check_num_b, int)):
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

    if (isinstance(check_num_a, int) and isinstance(check_num_b, int)):
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

    if (isinstance(check_num_a, int) and isinstance(check_num_b, int)):
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
    return IntNode(-self.visit(node.node).value) or FloatNode(-self.visit(node.node).value)

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