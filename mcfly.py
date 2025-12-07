from enum import Enum
import string
from dataclasses import dataclass

# Important Characters #

DIGITS  = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS_US = LETTERS + DIGITS + '_'

# Dictionary #

important_numbers = {
  '#pi': 3.141592653589793,
  '#tau': 6.283185307179586,
  '#e': 2.718281828459045
}

custom_numbers = {}

custom_strings = {}

custom_arrays = {}

important_words = {
  'fun': 'Coming Soon: The word fun is reserved for creating custom functions.',
  'if': 'Coming Soon: The word if is reserved for conditionals.',
  'sum': 'Coming Soon: The word sum is reserved for adding all the numbers in a set together.',
  'mean': 'Coming Soon: The term mean is reserved for calculating the mean of a set numbers.'
}

error_words = {
  'and': 'Error: Code can not start with the word and.',
  'or': 'Error: Code can not start with the word or.'
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
  LBRACKET       = 8
  RBRACKET       = 9
  ASSIGN         = 10
  NUMBER_VAR     = 11
  STRING_VAR     = 12
  ARRAY_VAR      = 13
  TYPE_EQUAL     = 14
  GT             = 15
  LT             = 16
  GTE            = 17
  LTE            = 18
  NE             = 19
  MATH_EQUALS    = 20
  TNE            = 21
  STRING         = 22
  NUMBER_TYPE    = 23
  INTEGER_TYPE   = 24
  FLOAT_TYPE     = 25
  STRING_TYPE    = 26
  EVEN_CHECK     = 27
  ODD_CHECK      = 28
  POSITIVE_CHECK = 29
  NEGATIVE_CHECK = 30
  AND_BOOLEAN    = 31
  NAND_BOOLEAN   = 32
  OR_BOOLEAN     = 33
  XOR_BOOLEAN    = 34
  NOR_BOOLEAN    = 35
  NOT_BOOLEAN    = 36
  TRUE           = 37
  FALSE          = 38
  FUNCTION       = 39
  CONDITIONAL    = 40
  ELSE           = 41
  ELIF           = 42
  SUM            = 43
  PRODUCT        = 44
  MEAN           = 45
  MEDIAN         = 46
  MODE           = 47
  MAX            = 48
  MIN            = 49
  SQUARE         = 50
  SQUARE_ROOT    = 51
  ROUND          = 52
  CEIL           = 53
  FLOOR          = 54
  ABSOLUTE_VALUE = 55
  ERROR_WORDS    = 56

# Lexer #

class Lexer:
  def __init__(self, text):
    self.text = text
    self.pos = 0
    self.current_char = text[0] if text else None

  def advance(self):
    self.pos += 1
    if self.pos < len(self.text):
      self.current_char = self.text[self.pos]
    else:
      self.current_char = None

  def show_error_words(self, prefix=''):
    error_words_str = self.current_char
    self.advance()

    while self.current_char != None:

      error_words_str += self.current_char
      self.advance()

    return prefix + error_words_str

  def lastCharCheckAdvance(self, char):
    if self.current_char == char:
      self.advance()

  def generate_tokens(self):
    while self.current_char != None:
      if self.current_char.isspace():
        self.advance()
        continue
      elif self.current_char.isdigit() or self.current_char == '.':
        yield self.generate_number()
      elif self.current_char == '#':
        self.advance()
        yield self.generate_num_var()
      elif self.current_char == '$':
        self.advance()
        yield self.generate_str_var()
      elif self.current_char == '@':
        self.advance()
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
        yield self.generate_equals()
      elif self.current_char == '>':
        self.advance()
        yield self.generate_greater_equal()
      elif self.current_char == '<':
        self.advance()
        yield self.generate_less_equal()
      elif self.current_char == '!':
        yield self.generate_not_equal()
      elif self.current_char.isalpha():
        word = self.collect_word()
        upper_word = word.upper()
        if upper_word == "TRUE":
          yield Token(TokenType.TRUE, True)
        elif upper_word == "FALSE":
          yield Token(TokenType.FALSE, False)
        elif upper_word == "NUM?":
          yield Token(TokenType.NUMBER_TYPE)
        elif upper_word == "INT?":
          yield Token(TokenType.INTEGER_TYPE)
        elif upper_word == "FLOAT?":
          yield Token(TokenType.FLOAT_TYPE)
        elif upper_word == "STR?":
          yield Token(TokenType.STRING_TYPE)
        elif upper_word == "ODD?":
          yield Token(TokenType.ODD_CHECK)
        elif upper_word == "EVEN?":
          yield Token(TokenType.EVEN_CHECK)
        elif upper_word == "POSITIVE?":
          yield Token(TokenType.POSITIVE_CHECK)
        elif upper_word == "NEGATIVE?":
          yield Token(TokenType.NEGATIVE_CHECK)
        elif upper_word == "ROUND":
          yield Token(TokenType.ROUND)
        elif upper_word == "CEIL":
          yield Token(TokenType.CEIL)
        elif upper_word == "FLOOR":
          yield Token(TokenType.FLOOR)
        elif upper_word == "ABS":
          yield Token(TokenType.ABSOLUTE_VALUE)
        elif upper_word == "SQUARE":
          yield Token(TokenType.SQUARE)
        elif upper_word == "SQRT":
          yield Token(TokenType.SQUARE_ROOT)
        elif upper_word == "SUM":
          yield Token(TokenType.SUM)
        elif upper_word == "PRODUCT":
          yield Token(TokenType.PRODUCT)
        elif upper_word == " MEAN":
          yield Token(TokenType.MEAN)
        elif upper_word == "NOT":
          yield Token(TokenType.NOT_BOOLEAN)
        elif upper_word == "AND":
          yield Token(TokenType.AND_BOOLEAN)
        elif upper_word == "NAND":
          yield Token(TokenType.NAND_BOOLEAN)
        elif upper_word == "OR":
          yield Token(TokenType.OR_BOOLEAN)
        elif upper_word == "XOR":
          yield Token(TokenType.XOR_BOOLEAN)
        elif upper_word == "NOR":
          yield Token(TokenType.NOR_BOOLEAN)
        elif upper_word == "IF":
          yield Token(TokenType.CONDITIONAL)
        elif upper_word == "ELSE":
          yield Token(TokenType.ELSE)
        elif upper_word == "ELIF":
          yield Token(TokenType.ELIF)
        elif upper_word == "FUN":
          yield Token(TokenType.FUNCTION)
      elif self.current_char in LETTERS:
        yield self.generate_error_words()
      else:
        raise Exception(f"llegal Character '{self.current_char}'")

  def generate_number(self):
    decimal_point_count = 0
    number_str = ""

    if self.current_char == '.':
      decimal_point_count = 1
      number_str = "0."
      self.advance()
    else:
      number_str = self.current_char
      self.advance()

    while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
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

    if string_str.endswith('"'):
      return Token(TokenType.STRING, str(string_str))
    else:
     raise Exception('Error: To print or use a string the input has to start with a " and end with a "')

  def generate_num_var(self):
    if not self.current_char.isalpha():
      raise Exception("Number variable must start with a letter after '#'")

    var_name = "#" + self.current_char
    self.advance()

    while (
      self.current_char is not None and
      (self.current_char.isalnum() or self.current_char == "_")
    ):
      var_name += self.current_char
      self.advance()

    return Token(TokenType.NUMBER_VAR, var_name)


  def generate_str_var(self):
    if not self.current_char.isalpha():
      raise Exception("String variable must start with a letter after '$'")

    var_name = "$" + self.current_char
    self.advance()

    while (
      self.current_char is not None and
      (self.current_char.isalnum() or self.current_char == "_")
    ):
      var_name += self.current_char
      self.advance()

    return Token(TokenType.STRING_VAR, var_name)

  def generate_array_var(self):
    if not self.current_char.isalpha():
      raise Exception("Array variable must start with a letter after '@'")

    var_name = "@" + self.current_char
    self.advance()

    while (
      self.current_char is not None and
      (self.current_char.isalnum() or self.current_char == "_")
    ):
      var_name += self.current_char
      self.advance()

    return Token(TokenType.ARRAY_VAR, var_name)

  def generate_equals(self):
    self.advance()
    if self.current_char == '=':
      self.advance()
      if self.current_char == '=':
        self.advance()
        return Token(TokenType.TYPE_EQUAL)
      else:
        return Token(TokenType.MATH_EQUALS)

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
      if self.current_char == '=':
        self.advance()
        return Token(TokenType.TNE)
      else:
        return Token(TokenType.NE)

  def generate_error_words(self):
    return Token(TokenType.ERROR_WORDS, self.show_error_words(''))

  def collect_word(self):
    """Collects letters plus allowed keyword suffix characters."""
    result = ''
    while (
      self.current_char is not None and (self.current_char.isalpha() or self.current_char in ['?'])
    ):
      result += self.current_char
      self.advance()
    return result

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
    return f"{self.value}"

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
    return f"({self.node_x}==={self.node_y})"

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
    return f"({self.node_x}!=={self.node_y})"

@dataclass
class NumberTypeNode:
  node: any

  def __repr__(self):
    return f"(num?{self.node})"

@dataclass
class IntegerTypeNode:
  node: any

  def __repr__(self):
    return f"(int?{self.node})"

@dataclass
class FloatTypeNode:
  node: any

  def __repr__(self):
    return f"(float?{self.node})"

@dataclass
class EvenCheckNode:
  node: any

  def __repr__(self):
    return f"(even?{self.node})"

@dataclass
class OddCheckNode:
  node: any

  def __repr__(self):
    return f"(odd?{self.node})"

@dataclass
class PositiveCheckNode:
  node: any

  def __repr__(self):
    return f"(positive?{self.node})"

@dataclass
class NegativeCheckNode:
  node: any

  def __repr__(self):
    return f"(negative?{self.node})"

@dataclass
class StringTypeNode:
  node: any

  def __repr__(self):
    return f"(str?{self.node})"

@dataclass
class AndBooleanNode:
  node_x: any
  node_y: any

  def __repr__(self):
    return f"{self.node_x} and {self.node_y}"

@dataclass
class NandBooleanNode:
  node_x: any
  node_y: any

  def __repr__(self):
    return f"{self.node_x} nand {self.node_y}"

@dataclass
class OrBooleanNode:
  node_x: any
  node_y: any

  def __repr__(self):
    return f"{self.node_x} or {self.node_y}"

@dataclass
class XorBooleanNode:
  node_x: any
  node_y: any

  def __repr__(self):
    return f"{self.node_x} xor {self.node_y}"

@dataclass
class NorBooleanNode:
  node_x: any
  node_y: any

  def __repr__(self):
    return f"{self.node_x} nor {self.node_y}"

@dataclass
class NotBooleanNode:
  node: any

  def __repr__(self):
    return f"not {self.node}"

@dataclass
class BooleanNode:
  value: bool

  def __repr__(self):
    return "True" if self.value else "False"

@dataclass
class FunctionNode:
  value: str
  WordFun = important_words['fun']

  def __repr__(self):
    if self.value:
      return f"{self.value}"
    return 'fun'

@dataclass
class ConditionalNode:
  value: str
  WordIf = important_words['if']

  def __repr__(self):
    if self.value:
      return f"{self.value}"
    return 'if'

@dataclass
class SumNode:
  value: str
  WordSum = important_words['sum']

  def __repr__(self):
    if self.value:
      return f"{self.value}"
    return 'sum'

@dataclass
class MeanNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"(({self.node_a}+{self.node_b})/2)"

@dataclass
class SquareNode:
  node: any

  def __repr__(self):
    return f"square {self.node}"

@dataclass
class SquareRootNode:
  node: any

  def __repr__(self):
    return f"sqrt {self.node}"

@dataclass
class AbsoluteValueNode:
  node: any

  def __repr__(self):
    return f"abs {self.node}"

@dataclass
class CeilNode:
  node: any

  def __repr__(self):
    return f"(ceil{self.node})"

@dataclass
class FloorNode:
  node: any

  def __repr__(self):
    return f"(floor{self.node})"

@dataclass
class ErrorWordsNode:
  value: str
  ErrorAnd = error_words['and']
  ErrorOr = error_words['or']

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
    result = self.andCheck()

    while self.current_token != None and self.current_token.type in (TokenType.MATH_EQUALS, TokenType.MATH_EQUALS):
      if self.current_token.type == TokenType.MATH_EQUALS:
        self.advance()
        result = MathEqualNode(result, self.andCheck())

    return result

  def andCheck(self):
    result = self.orCheck()

    while self.current_token != None and self.current_token.type in (TokenType.AND_BOOLEAN, TokenType.AND_BOOLEAN):
      if self.current_token.type == TokenType.AND_BOOLEAN:
        self.advance()
        result = AndBooleanNode(result, self.orCheck())

    return result

  def orCheck(self):
    result = self.xorCheck()

    while self.current_token != None and self.current_token.type in (TokenType.OR_BOOLEAN, TokenType.OR_BOOLEAN):
      if self.current_token.type == TokenType.OR_BOOLEAN:
        self.advance()
        result = OrBooleanNode(result, self.xorCheck())

    return result

  def xorCheck(self):
    result = self.nandCheck()

    while self.current_token != None and self.current_token.type in (TokenType.XOR_BOOLEAN, TokenType.XOR_BOOLEAN):
      if self.current_token.type == TokenType.XOR_BOOLEAN:
        self.advance()
        result = XorBooleanNode(result, self.nandCheck())

    return result

  def nandCheck(self):
    result = self.norCheck()

    while self.current_token != None and self.current_token.type in (TokenType.NAND_BOOLEAN, TokenType.NAND_BOOLEAN):
      if self.current_token.type == TokenType.NAND_BOOLEAN:
        self.advance()
        result = NandBooleanNode(result, self.norCheck())

    return result

  def norCheck(self):
    result = self.meanCheck()

    while self.current_token != None and self.current_token.type in (TokenType.NOR_BOOLEAN, TokenType.NOR_BOOLEAN):
      if self.current_token.type == TokenType.NOR_BOOLEAN:
        self.advance()
        result = NorBooleanNode(result, self.meanCheck())

    return result

  def meanCheck(self):
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.MEAN, TokenType.MEAN):
      if self.current_token.type == TokenType.MEAN:
        self.advance()
        result = MeanNode(result, self.factor())

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

    if token.type == TokenType.INTEGER:
      self.advance()
      return IntNode(token.value)

    if token.type == TokenType.FLOAT:
      self.advance()
      return FloatNode(token.value)

    if token.type == TokenType.STRING:
      self.advance()
      return StringNode(token.value)

    if token.type == TokenType.NUMBER_VAR:
      self.advance()
      return NumberSignNode(token.value)

    if token.type == TokenType.STRING_VAR:
      self.advance()
      return StringSignNode(token.value)

    if token.type == TokenType.ARRAY_VAR:
      self.advance()
      return ArraySignNode(token.value)

    if token.type == TokenType.TRUE:
      self.advance()
      return BooleanNode(token.value)

    if token.type == TokenType.FALSE:
      self.advance()
      return BooleanNode(token.value)

    if token.type == TokenType.PLUS:
      self.advance()
      return PlusNode(self.factor())

    if token.type == TokenType.MINUS:
      self.advance()
      return MinusNode(self.factor())

    if token.type == TokenType.NOT_BOOLEAN:
      self.advance()
      return NotBooleanNode(self.factor())

    if token.type == TokenType.NUMBER_TYPE:
      self.advance()
      return NumberTypeNode(self.factor())

    if token.type == TokenType.INTEGER_TYPE:
      self.advance()
      return IntegerTypeNode(self.factor())

    if token.type == TokenType.FLOAT_TYPE:
      self.advance()
      return FloatTypeNode(self.factor())

    if token.type == TokenType.STRING_TYPE:
      self.advance()
      return StringTypeNode(self.factor())

    if token.type == TokenType.EVEN_CHECK:
      self.advance()
      return EvenCheckNode(self.factor())

    if token.type == TokenType.ODD_CHECK:
      self.advance()
      return OddCheckNode(self.factor())

    if token.type == TokenType.POSITIVE_CHECK:
      self.advance()
      return PositiveCheckNode(self.factor())

    if token.type == TokenType.NEGATIVE_CHECK:
      self.advance()
      return NegativeCheckNode(self.factor())

    if token.type == TokenType.CEIL:
      self.advance()
      return CeilNode(self.factor())

    if token.type == TokenType.FLOOR:
      self.advance()
      return FloorNode(self.factor())

    if token.type == TokenType.SQUARE:
      self.advance()
      return SquareNode(self.factor())

    if token.type == TokenType.SQUARE_ROOT:
      self.advance()
      return SquareRootNode(self.factor())

    if token.type == TokenType.ABSOLUTE_VALUE:
      self.advance()
      return AbsoluteValueNode(self.factor())

    if token.type == TokenType.FUNCTION:
      self.advance()
      return FunctionNode(token.value)
    elif token.type == TokenType.CONDITIONAL:
      self.advance()
      return ConditionalNode(token.value)
    elif token.type == TokenType.SUM:
      self.advance()
      return SumNode(token.value)
    elif token.type == TokenType.ERROR_WORDS:
      self.advance()
      return ErrorWordsNode(token.value)
    self.raise_error()

# Interpreter #

class Interpreter:
  def visit(self, node):
    method_name = f'visit_{type(node).__name__}'
    method = getattr(self, method_name)
    return method(node)

  def visit_IntNode(self, node):
    if isinstance(node.value, int):
      return IntNode(node.value)

  def visit_FloatNode(self, node):
    if isinstance(node.value, float):
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
    NVFLQ = NV[1:-1]

    return StringNode(NVFLQ)

  def visit_FunctionNode(self, node):
      return FunctionNode(node.WordFun)

  def visit_ConditionalNode(self, node):
      return ConditionalNode(node.WordIf)

  def visit_SumNode(self, node):
      return SumNode(node.WordSum)

  def visit_MeanNode(self, node):
    check_num_a = self.visit(node.node_a).value
    check_num_b = self.visit(node.node_b).value

    if isinstance(check_num_a, int) and isinstance(check_num_b, int):
      total = check_num_a + check_num_b
      if ((total % 2) == 0):
       return IntNode(int(total/2))
      else:
        return FloatNode(total/2)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
      total = check_num_a + check_num_b
      return FloatNode(total/2)
    elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
      total = check_num_a + check_num_b
      return FloatNode(total/2)
    elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
      total = check_num_a + check_num_b
      return FloatNode(total/2)

  def visit_SquareNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
      return IntNode(check_num * check_num)
    elif isinstance(check_num, float):
      return FloatNode(check_num * check_num)

  def visit_SquareRootNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
      answer = (check_num**(1/2))
      if ((answer % 1) == 0):
        return IntNode(int(answer))
      else:
        return FloatNode(answer)
    elif isinstance(check_num, float):
      answer = (check_num**(1/2))
      return FloatNode(answer)

  def visit_AbsoluteValueNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
      if check_num < 0:
        return IntNode(check_num*-1)
      else:
        return IntNode(check_num)
    elif isinstance(check_num, float):
      if check_num < 0:
        return FloatNode(check_num*-1)
      else:
        return FloatNode(check_num)

  def visit_CeilNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
      return IntNode(check_num)
    elif isinstance(check_num, float):
      if (((check_num % 1) == 0) or (check_num < 0)):
        return IntNode(int(check_num))
      elif check_num > 0:
        return IntNode(int(check_num)+1)

  def visit_FloorNode(self, node):
    check_num = self.visit(node.node).value

    if isinstance(check_num, int):
     return IntNode(check_num)
    elif isinstance(check_num, float):
      if (((check_num % 1) == 0) or (check_num > 0)):
        return IntNode(int(check_num))
      elif check_num < 0:
        return IntNode((int(check_num)-1))


  def visit_ErrorWordsNode(self, node):
    if node.value == 'and':
      return ErrorWordsNode(node.ErrorAnd)
    elif node.value == 'or':
      return ErrorWordsNode(node.ErrorOr)
    else:
      return 'Error: Not a Keyword'

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
      if check_x > check_y:
        return 'True'
      elif (check_x < check_y) or (check_x == check_y):
        return 'False'

  def visit_LessThanNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y) or (check_x == check_y):
        return 'False'
      elif check_x < check_y:
        return 'True'

  def visit_GreaterThanEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if (check_x > check_y) or (check_x == check_y):
        return 'True'
      elif check_x < check_y:
        return 'False'

  def visit_LessThanEqualNode(self, node):
    check_x = self.visit(node.node_x).value
    check_y = self.visit(node.node_y).value

    if (isinstance(check_x, int) or isinstance(check_x, float)) and (isinstance(check_y, int) or isinstance(check_y, float)):
      if check_x > check_y:
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
        quotient = check_num_a / check_num_b
        if ((quotient % 1) == 0):
          return IntNode(int(quotient))
        else:
          return FloatNode(quotient)
      elif isinstance(check_num_a, float) and isinstance(check_num_b, float):
        quotient = check_num_a / check_num_b
        if ((quotient % 1) == 0):
          return IntNode(int(quotient))
        else:
          return FloatNode(quotient)
      elif isinstance(check_num_a, int) and isinstance(check_num_b, float):
        quotient = check_num_a / check_num_b
        if ((quotient % 1) == 0):
          return IntNode(int(quotient))
        else:
          return FloatNode(quotient)
      elif isinstance(check_num_a, float) and isinstance(check_num_b, int):
        quotient = check_num_a / check_num_b
        if ((quotient % 1) == 0):
          return IntNode(int(quotient))
        else:
          return FloatNode(quotient)
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

    if isinstance(check_text, (int, float)):
      return BooleanNode(True)
    elif isinstance(check_text, str):
      return BooleanNode(False)

  def visit_IntegerTypeNode(self, node):
    check_text = self.visit(node.node).value

    if isinstance(check_text, int):
      return BooleanNode(True)
    else:
      return BooleanNode(False)

  def visit_FloatTypeNode(self, node):
    check_text = self.visit(node.node).value

    if isinstance(check_text, float):
      return BooleanNode(True)
    else:
      return BooleanNode(False)

  def visit_EvenCheckNode(self, node):
    check_text = self.visit(node.node).value

    if ((check_text % 2) == 0):
      return BooleanNode(True)
    else:
      return BooleanNode(False)

  def visit_OddCheckNode(self, node):
    check_text = self.visit(node.node).value

    if ((check_text % 2) == 0):
      return BooleanNode(False)
    else:
      return BooleanNode(True)

  def visit_PositiveCheckNode(self, node):
    check_text = self.visit(node.node).value

    if isinstance(check_text, (int, float)) and check_text > 0:
      return BooleanNode(True)
    else:
      return BooleanNode(False)

  def visit_NegativeCheckNode(self, node):
    check_text = self.visit(node.node).value

    if isinstance(check_text, (int, float)) and check_text < 0:
      return BooleanNode(True)
    else:
      return BooleanNode(False)

  def visit_StringTypeNode(self, node):
    check_text = self.visit(node.node).value

    if isinstance(check_text, str):
      return BooleanNode(True)
    elif isinstance(check_text, (int, float)):
      return BooleanNode(False)

  def visit_AndBooleanNode(self, node):
    if (isinstance(node.node_x, TrueNode)) and (isinstance(node.node_y, TrueNode)):
      return 'True'
    elif ((isinstance(node.node_x, TrueNode)) or (isinstance(node.node_x, FalseNode))) and ((isinstance(node.node_y, TrueNode)) or (isinstance(node.node_y, FalseNode))):
      return 'False'

  def visit_NandBooleanNode(self, node):
    if (isinstance(node.node_x, TrueNode)) and (isinstance(node.node_y, TrueNode)):
      return 'False'
    elif ((isinstance(node.node_x, TrueNode)) or (isinstance(node.node_x, FalseNode))) and ((isinstance(node.node_y, TrueNode)) or (isinstance(node.node_y, FalseNode))):
      return 'True'

  def visit_OrBooleanNode(self, node):
    if (isinstance(node.node_x, FalseNode)) and (isinstance(node.node_y, FalseNode)):
      return 'False'
    elif ((isinstance(node.node_x, TrueNode)) or (isinstance(node.node_x, FalseNode))) and ((isinstance(node.node_y, TrueNode)) or (isinstance(node.node_y, FalseNode))):
      return 'True'

  def visit_XorBooleanNode(self, node):
    if ((isinstance(node.node_x, TrueNode)) and (isinstance(node.node_y, TrueNode))) or ((isinstance(node.node_x, FalseNode)) and (isinstance(node.node_y, FalseNode))):
      return 'False'
    elif ((isinstance(node.node_x, TrueNode)) and (isinstance(node.node_y, FalseNode))) or ((isinstance(node.node_x, FalseNode)) and (isinstance(node.node_y, TrueNode))):
      return 'True'

  def visit_NorBooleanNode(self, node):
    if (isinstance(node.node_x, FalseNode)) and (isinstance(node.node_y, FalseNode)):
      return 'True'
    elif ((isinstance(node.node_x, TrueNode)) or (isinstance(node.node_x, FalseNode))) and ((isinstance(node.node_y, TrueNode)) or (isinstance(node.node_y, FalseNode))):
      return 'False'

  def visit_NotBooleanNode(self, node):
    if isinstance(node.node, TrueNode):
      return FalseNode(node.node)
    elif isinstance(node.node, FalseNode):
      return TrueNode(node.node)

  def visit_BooleanNode(self, node):
    return node.value

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