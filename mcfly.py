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
  '#tau': 6.28318531,
  '#e': 2.71828183
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
  TYPE_EQUAL     = 11
  GT             = 12
  LT             = 13
  GTE            = 14
  LTE            = 15
  NE             = 16
  MATH_EQUALS    = 17
  TNE            = 18
  STRING         = 19
  NUMBER_TYPE    = 20
  STRING_TYPE    = 21
  NOT_BOOLEAN    = 22
  KEYWORDS       = 23

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
      elif self.current_char == '"':
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
        yield self.generate_equal()
      elif self.current_char == '>':
        yield self.generate_greater_equal()
      elif self.current_char == '<':
        yield self.generate_less_equal()
      elif self.current_char == '!':
        yield self.generate_not_equal()
      elif self.current_char == 'n':
        yield self.generate_not_boolean()
      elif self.current_char in LETTERS:
        yield self.generate_keywords()
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

    if self.current_char == '#': 
      self.advance()
      return Token(TokenType.NUMBER_TYPE)
    else:
      return Token(TokenType.NUMBER_VAR, num_sign_var)

  def generate_str_var(self):
    str_sign_var = self.current_char
    self.advance()

    while self.current_char != None and self.current_char in LETTERS_DIGITS_US:
      str_sign_var += self.current_char
      self.advance()

    if self.current_char == '$': 
      self.advance()
      return Token(TokenType.STRING_TYPE)
    else:
      return Token(TokenType.STRING_VAR, str_sign_var)

  def generate_array_var(self):
    array_sign_var = self.current_char
    self.advance()

    while self.current_char != None and self.current_char in LETTERS_DIGITS_US:
      array_sign_var += self.current_char
      self.advance()

    return Token(TokenType.ARRAY_VAR, array_sign_var)

  def generate_equal(self):
    self.advance()
    if self.current_char == '=': 
      self.advance()
      return Token(TokenType.MATH_EQUALS)
    else:
      return Token(TokenType.TYPE_EQUAL)

  def generate_greater_equal(self):
    self.advance()
    if self.current_char == '=': 
      self.advance()
      return Token(TokenType.GTE)
    else:
      return Token(TokenType.GT)

  def generate_less_equal(self):
    self.advance()
    if self.current_char == '=': 
      self.advance()
      return Token(TokenType.LTE)
    else:
      return Token(TokenType.LT)

  def generate_not_equal(self):
    self.advance()
    if self.current_char == '=': 
      self.advance()
      return Token(TokenType.NE)
    else:
      return Token(TokenType.TNE)

  def generate_not_boolean(self):
    self.advance()
    if self.current_char == 'o': 
      self.advance()
      if self.current_char == 't':
        self.advance()
        return Token(TokenType.NOT_BOOLEAN)

  def generate_keywords(self):
    keywords_str = self.current_char
    self.advance()

    while self.current_char != None:

      keywords_str += self.current_char
      self.advance()

    return Token(TokenType.KEYWORDS, str(keywords_str))

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
  StartValueTau = important_numbers['#tau']
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
class TypeEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}={self.node_y})"

@dataclass
class MathEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}=={self.node_y})"

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

@dataclass
class GreaterThanEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}>={self.node_y})"

@dataclass
class LessThanEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}<={self.node_y})"

@dataclass
class NotEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}!={self.node_y})"

@dataclass
class TypeNotEqualNode:
  node_x: any
  node_y: any

  def __repr__(self): 
    return f"({self.node_x}!{self.node_y})"

@dataclass
class NumberTypeNode:
  node: any

  def __repr__(self):
    return f"(##{self.node})"

@dataclass
class StringTypeNode:
  node: any

  def __repr__(self):
    return f"($${self.node})"

@dataclass
class NotBooleanNode:
  node: any

  def __repr__(self):
    return f"(not{self.node})"

@dataclass
class KeywordsNode:
  value: str
  WordFun = important_words['fun']
  WordIf = important_words['if']  
  ErrorAnd = error_words['and']
  ErrorOr = error_words['or']
  WordSum = important_words['sum']
  WordAvg = important_words['avg']

  def __repr__(self):
    return f"{self.value}"

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
    result = self.typeEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.typeEqualCheck())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.typeEqualCheck())

    return result

  def typeEqualCheck(self):
    result = self.greaterCheck()

    while self.current_token != None and self.current_token.type in (TokenType.TYPE_EQUAL, TokenType.TYPE_EQUAL):
      if self.current_token.type == TokenType.TYPE_EQUAL:
        self.advance()
        result = TypeEqualNode(result, self.greaterCheck())

    return result

  def greaterCheck(self):
    result = self.lessCheck()

    while self.current_token != None and self.current_token.type in (TokenType.GT, TokenType.GT):
      if self.current_token.type == TokenType.GT:
        self.advance()
        result = GreaterThanNode(result, self.lessCheck())

    return result

  def lessCheck(self):
    result = self.greaterEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.LT, TokenType.LT):
      if self.current_token.type == TokenType.LT:
        self.advance()
        result = LessThanNode(result, self.greaterEqualCheck())

    return result

  def greaterEqualCheck(self):
    result = self.lessEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.GTE, TokenType.GTE):
      if self.current_token.type == TokenType.GTE:
        self.advance()
        result = GreaterThanEqualNode(result, self.lessEqualCheck())

    return result

  def lessEqualCheck(self):
    result = self.notEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.LTE, TokenType.LTE):
      if self.current_token.type == TokenType.LTE:
        self.advance()
        result = LessThanEqualNode(result, self.notEqualCheck())

    return result

  def notEqualCheck(self):
    result = self.typeNotEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.NE, TokenType.NE):
      if self.current_token.type == TokenType.NE:
        self.advance()
        result = NotEqualNode(result, self.typeNotEqualCheck())

    return result

  def typeNotEqualCheck(self):
    result = self.mathEqualCheck()

    while self.current_token != None and self.current_token.type in (TokenType.TNE, TokenType.TNE):
      if self.current_token.type == TokenType.TNE:
        self.advance()
        result = TypeNotEqualNode(result, self.mathEqualCheck())

    return result

  def mathEqualCheck(self):
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.MATH_EQUALS, TokenType.MATH_EQUALS):
      if self.current_token.type == TokenType.MATH_EQUALS:
        self.advance()
        result = MathEqualNode(result, self.factor())

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
    elif token.type == TokenType.NUMBER_TYPE:
      self.advance()
      return NumberTypeNode(self.factor())
    elif token.type == TokenType.STRING_TYPE:
      self.advance()
      return StringTypeNode(self.factor())
    elif token.type == TokenType.NOT_BOOLEAN:
      self.advance()
      return NotBooleanNode(self.factor())
    elif token.type == TokenType.KEYWORDS:
      self.advance()
      return KeywordsNode(token.value)  
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
    elif node.value == '#tau':
      return NumberSignNode(node.StartValueTau)
    elif node.value == '#e':
      return NumberSignNode(node.StartValueE)
    else:
      return NumberSignNode(node.value)

  def visit_StringSignNode(self, node):
    return StringSignNode(node.value)

  def visit_ArraySignNode(self, node):
    return ArraySignNode(node.value)

  def visit_StringNode(self, node):
    NV = node.value
    NVF = NV.replace('"', '', 1)

    return StringNode(NVF)

  def visit_KeywordsNode(self, node):

    if node.value == 'fun':
      return KeywordsNode(node.WordFun)
    elif node.value == 'if':
      return KeywordsNode(node.WordIf)    
    elif node.value == 'and':
      return KeywordsNode(node.ErrorAnd)
    elif node.value == 'or':
      return KeywordsNode(node.ErrorOr)
    elif node.value == 'sum':
      return KeywordsNode(node.WordSum)
    elif node.value == 'avg':
      return KeywordsNode(node.WordAvg)

  def visit_TypeEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) and isinstance(check_y, int)) or (isinstance(check_x, float) and isinstance(check_y, float)):
      if check_x == check_y:
        return 'True'
      else:
        return 'False'
    elif (isinstance(check_x, int) and isinstance(check_y, float)) or (isinstance(check_x, float) and isinstance(check_y, int)):
      return 'False'

  def visit_MathEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if check_x == check_y:
        return 'True'
      elif check_x != check_y:
        return 'False'

  def visit_GreaterThanNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y):
        return 'True'
      elif (check_x < check_y) or (check_x == check_y):
        return 'False'

  def visit_LessThanNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y) or (check_x == check_y):
        return 'False'
      elif (check_x < check_y):
        return 'True'

  def visit_GreaterThanEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y) or (check_x == check_y):
        return 'True'
      elif (check_x < check_y):
        return 'False'

  def visit_LessThanEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y):
        return 'False'
      elif (check_x < check_y) or (check_x == check_y):
        return 'True'

  def visit_NotEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if check_x != check_y:
        return 'True'
      elif check_x == check_y:
        return 'False'

  def visit_TypeNotEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) and isinstance(check_y, int)) or (isinstance(check_x, float) and isinstance(check_y, float)):
      if check_x == check_y:
        return 'False'
      else:
        return 'True'
    elif (isinstance(check_x, int) and isinstance(check_y, float)) or (isinstance(check_x, float) and isinstance(check_y, int)):
        return 'True'

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
  
  def visit_NumberTypeNode(self, node):
    check_text = self.visit(node.node).value
    
    if isinstance(check_text, int) or isinstance(check_text, float):
      return 'True'
    elif isinstance(check_text, str):
      return 'False'
      
  def visit_StringTypeNode(self, node):
    check_text = self.visit(node.node).value
    
    if isinstance(check_text, str):
      return 'True'
    elif isinstance(check_text, int) or isinstance(check_text, float):
      return 'False'

  def visit_NotBooleanNode(self, node):
    check_text = self.visit(node.node).value
    
    if check_text == 'True':
      return 'False'
    elif check_text == 'False':
      return 'True'

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