from enum import Enum
import string

# Important Characters #

WHITESPACE = ' \n\t'
DIGITS  = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

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
    number_sign_count = 0
    num_sign_var = self.current_char
    self.advance()

    while self.current_char != None:
      if self.current_char == '#': 
        number_sign_count += 1
        if number_sign_count > 1:
          break

      num_sign_var += self.current_char
      self.advance()

    if num_sign_var.startswith('#') and number_sign_count == 1:
      num_sign_var = num_sign_var

    return Token(TokenType.NUMBER_VAR, str(num_sign_var))

  def generate_str_var(self):
    string_sign_count = 0
    str_sign_var = self.current_char
    self.advance()

    while self.current_char != None:
      if self.current_char == '$': 
        string_sign_count += 1
        if string_sign_count > 1:
          break

      str_sign_var += self.current_char
      self.advance()

    if str_sign_var.startswith('$'):
      str_sign_var = str_sign_var

    return Token(TokenType.STRING_VAR, str(str_sign_var))

  def generate_array_var(self):
    array_sign_count = 0
    array_sign_var = self.current_char
    self.advance()

    while self.current_char != None:
      if self.current_char == '@': 
        array_sign_count += 1
        if array_sign_count > 1:
          break

      array_sign_var += self.current_char
      self.advance()

    if array_sign_var.startswith('@'):
      array_sign_var = array_sign_var

    return Token(TokenType.ARRAY_VAR, str(array_sign_var))

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
      equal_sign = equal_sign

    return Token(TokenType.EQUAL, str(equal_sign))