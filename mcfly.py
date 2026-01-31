from enum import Enum, auto
from dataclasses import dataclass

# Dictionary #

important_numbers = {
  '#pi': 3.141592653589793,
  '#tau': 6.283185307179586,
  '#e': 2.718281828459045
}

custom_strings = {}

custom_arrays = {}

important_words = {
  'fun': 'Coming Soon: The word fun is reserved for creating custom functions.',
}

# Tokens #

class TokenType(Enum):
  INTEGER        = auto()
  FLOAT          = auto()
  PLUS           = auto()
  MINUS          = auto()
  MULTIPLY       = auto()
  DIVIDE         = auto()
  LPAREN         = auto()
  RPAREN         = auto()
  LBRACKET       = auto()
  RBRACKET       = auto()
  COMMA          = auto()
  ASSIGN         = auto()
  NUMBER_VAR     = auto()
  STRING_VAR     = auto()
  ARRAY_VAR      = auto()
  TYPE_EQUAL     = auto()
  GT             = auto()
  LT             = auto()
  GTE            = auto()
  LTE            = auto()
  NE             = auto()
  EQUALS         = auto()
  TNE            = auto()
  STRING         = auto()
  NUMBER_TYPE    = auto()
  INTEGER_TYPE   = auto()
  FLOAT_TYPE     = auto()
  STRING_TYPE    = auto()
  EVEN_CHECK     = auto()
  ODD_CHECK      = auto()
  POSITIVE_CHECK = auto()
  NEGATIVE_CHECK = auto()
  AND_BOOLEAN    = auto()
  NAND_BOOLEAN   = auto()
  OR_BOOLEAN     = auto()
  XOR_BOOLEAN    = auto()
  NOR_BOOLEAN    = auto()
  NOT_BOOLEAN    = auto()
  TRUE           = auto()
  FALSE          = auto()
  FUNCTION       = auto()
  CONDITIONAL    = auto()
  ELSE           = auto()
  ELIF           = auto()
  COLON          = auto()
  END            = auto()
  SUM            = auto()
  PRODUCT        = auto()
  MEAN           = auto()
  MEDIAN         = auto()
  MODE           = auto()
  MAX            = auto()
  MIN            = auto()
  RANGE          = auto()
  SQUARE         = auto()
  SQUARE_ROOT    = auto()
  ROUND          = auto()
  CEIL           = auto()
  FLOOR          = auto()
  ABSOLUTE_VALUE = auto()
  PRINT          = auto()
  ERROR_WORDS    = auto()

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
      elif self.current_char == '[':
        self.advance()
        yield Token(TokenType.LBRACKET)
      elif self.current_char == ']':
        self.advance()
        yield Token(TokenType.RBRACKET)
      elif self.current_char == ',':
        self.advance()
        yield Token(TokenType.COMMA)
      elif self.current_char == '=':
        yield self.generate_equals()
      elif self.current_char == '>':
        yield self.generate_greater_equal()
      elif self.current_char == '<':
        yield self.generate_less_equal()
      elif self.current_char == '!':
        yield self.generate_not_equal()
      elif self.current_char == ':':
        self.advance()
        yield Token(TokenType.COLON)
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
        elif upper_word == "MEAN":
          yield Token(TokenType.MEAN)
        elif upper_word == "MEDIAN":
          yield Token(TokenType.MEDIAN)
        elif upper_word == "MODE":
          yield Token(TokenType.MODE)
        elif upper_word == "MAX":
          yield Token(TokenType.MAX)
        elif upper_word == "MIN":
          yield Token(TokenType.MIN)
        elif upper_word == "RANGE":
          yield Token(TokenType.RANGE)
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
        elif upper_word == "END":
          yield Token(TokenType.END)
        elif upper_word == "PRINT":
          yield Token(TokenType.PRINT)
        else:
          yield Token(TokenType.ERROR_WORDS, word)

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
    self.advance()
    string = ""

    while self.current_char is not None and self.current_char != '"':
      string += self.current_char
      self.advance()

    self.advance()

    return Token(TokenType.STRING, string)

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

      return Token(TokenType.EQUALS)

    return Token(TokenType.ASSIGN)

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
class ArrayNode:
  elements: list

  def __repr__(self):
    elementsList = ", ".join(map(str, self.elements))
    return f"[{elementsList}]"

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
class AssignNode:
  var_type: TokenType
  name: str
  value: any

  def __repr__(self):
    return f"({self.name} = {self.value})"

@dataclass
class NumberSignNode:
  value: str

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
class EqualNode:
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
class ASTNode:
    pass

@dataclass
class FunctionNode:
  name: str
  params: list[str]
  body: "ASTNode"

  def __repr__(self):
    params = ", ".join(self.params)
    return f"fun {self.name}({params}): {self.body} end"

@dataclass
class ConditionalNode:
  cases: list[tuple[object, object]]
  else_case: object | None = None

  def __post_init__(self):
    if not self.cases:
      raise ValueError("ConditionalNode requires at least one IF case")

  def __repr__(self):
    parts = []

    # IF or ELIF cases
    for i, (condition, expr) in enumerate(self.cases):
      if i == 0:
        parts.append(f"if {condition}: {expr}")
      else:
        parts.append(f"elif {condition}: {expr}")

    # ELSE case
    if self.else_case is not None:
      parts.append(f"else: {self.else_case}")

    parts.append("end")
    return " ".join(parts)

@dataclass
class SumNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"sum({valuesList})"

@dataclass
class ProductNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"product({valuesList})"

@dataclass
class MeanNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"mean({valuesList})"

@dataclass
class MedianNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"median({valuesList})"

@dataclass
class ModeNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"mode({valuesList})"

@dataclass
class MaxNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"max({valuesList})"

@dataclass
class MinNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"min({valuesList})"

@dataclass
class RangeNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"range({valuesList})"

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
class RoundNode:
  value: any
  precision: any = None

  def __repr__(self):
    if self.precision is None:
      return f"(round {self.value})"
    return f"(round {self.value}, {self.precision})"

@dataclass
class PrintNode:
  value: any

  def __repr__(self):
    return f"(print {self.value})"

@dataclass
class ErrorWordsNode:
  value: str

  def __repr__(self):
    return f"{self.value}"

# Parser #

class Parser:
  def __init__(self, tokens):
    self.tokens = list(tokens)
    self.token_index = 0
    self.current_token = self.tokens[0] if self.tokens else None

  def raise_error(self):
    raise Exception("Invalid Syntax")

  def advance(self):
    self.token_index += 1
    if self.token_index < len(self.tokens):
      self.current_token = self.tokens[self.token_index]
    else:
      self.current_token = None

  def eat(self, token_type):
    if self.current_token is not None and self.current_token.type == token_type:
      self.advance()
    else:
      raise Exception(
        f"Expected token {token_type}, got "
        f"{self.current_token.type if self.current_token else 'None'}"
      )

  def expect(self, token_type):
    if self.current_token is None:
      self.raise_error()

    if self.current_token.type != token_type:
      self.raise_error()

    self.advance()

  def parse(self):
    if self.current_token is None:
      return None

    # Function definitions disabled until fully implemented
    # if self.current_token.type == TokenType.FUNCTION:
    #     result = self.function_definition()
    # else:
    result = self.statement()

    if self.current_token is not None:
      self.raise_error()

    return result

  def function_definition(self):
    self.expect(TokenType.FUNCTION)  # fun
    name = self.expect(TokenType.IDENTIFIER).value

    self.expect(TokenType.LPAREN)
    params = []
    self.expect(TokenType.RPAREN)

    self.expect(TokenType.EQUAL)
    body = self.statement()

    return FunctionNode(name, params, body)

  def statement(self):
    if self.current_token.type == TokenType.PRINT:
      return self.print_statement()

    if (self.current_token.type in (
      TokenType.NUMBER_VAR,
      TokenType.STRING_VAR,
      TokenType.ARRAY_VAR,
    ) and self.peek() is not None and self.peek().type == TokenType.ASSIGN):
      return self.assignment()

    return self.expr()

  def print_statement(self):
    self.expect(TokenType.PRINT)

    token = self.current_token

    if token.type not in (
      TokenType.NUMBER_VAR,
      TokenType.STRING_VAR,
      TokenType.ARRAY_VAR,
    ):
      raise Exception("Syntax Error: print expects a variable")

    self.advance()

    return PrintNode(token.value)

  def peek(self):
    if self.token_index + 1 < len(self.tokens):
      return self.tokens[self.token_index + 1]
    return None

  def assignment(self):
    var_token = self.current_token
    name = var_token.value
    self.advance()

    self.expect(TokenType.ASSIGN)

    value = self.expr()

    return AssignNode(var_token.type, name, value)

  def expr(self):
    result = self.term()

    while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
      if self.current_token.type == TokenType.PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif self.current_token.type == TokenType.MINUS:
        self.advance()
        result = SubtractNode(result, self.term())

    return result

  def term(self):
    result = self.typeEqualCheck()

    while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.typeEqualCheck())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.typeEqualCheck())

    return result

  def typeEqualCheck(self):
    result = self.greaterCheck()

    while self.current_token is not None and self.current_token.type == TokenType.TYPE_EQUAL:
      self.advance()
      result = TypeEqualNode(result, self.greaterCheck())

    return result

  def greaterCheck(self):
    result = self.lessCheck()

    while self.current_token is not None and self.current_token.type == TokenType.GT:
      self.advance()
      result = GreaterThanNode(result, self.lessCheck())

    return result

  def lessCheck(self):
    result = self.greaterEqualCheck()

    while self.current_token is not None and self.current_token.type == TokenType.LT:
      self.advance()
      result = LessThanNode(result, self.greaterEqualCheck())

    return result

  def greaterEqualCheck(self):
    result = self.lessEqualCheck()

    while self.current_token is not None and self.current_token.type == TokenType.GTE:
      self.advance()
      result = GreaterThanEqualNode(result, self.lessEqualCheck())

    return result

  def lessEqualCheck(self):
    result = self.notEqualCheck()

    while self.current_token is not None and self.current_token.type == TokenType.LTE:
      self.advance()
      result = LessThanEqualNode(result, self.notEqualCheck())

    return result

  def notEqualCheck(self):
    result = self.typeNotEqualCheck()

    while self.current_token is not None and self.current_token.type == TokenType.NE:
      self.advance()
      result = NotEqualNode(result, self.typeNotEqualCheck())

    return result

  def typeNotEqualCheck(self):
    result = self.equalCheck()

    while self.current_token is not None and self.current_token.type == TokenType.TNE:
      self.advance()
      result = TypeNotEqualNode(result, self.equalCheck())

    return result

  def equalCheck(self):
    result = self.andCheck()

    while self.current_token is not None and self.current_token.type == TokenType.EQUALS:
      self.advance()
      result = EqualNode(result, self.andCheck())

    return result

  def andCheck(self):
    result = self.orCheck()

    while self.current_token is not None and self.current_token.type == TokenType.AND_BOOLEAN:
      self.advance()
      result = AndBooleanNode(result, self.orCheck())

    return result

  def orCheck(self):
    result = self.xorCheck()

    while self.current_token is not None and self.current_token.type == TokenType.OR_BOOLEAN:
      self.advance()
      result = OrBooleanNode(result, self.xorCheck())

    return result

  def xorCheck(self):
    result = self.nandCheck()

    while self.current_token is not None and self.current_token.type == TokenType.XOR_BOOLEAN:
      self.advance()
      result = XorBooleanNode(result, self.nandCheck())

    return result

  def nandCheck(self):
    result = self.norCheck()

    while self.current_token is not None and self.current_token.type == TokenType.NAND_BOOLEAN:
      self.advance()
      result = NandBooleanNode(result, self.norCheck())

    return result

  def norCheck(self):
    result = result = self.factor()

    while self.current_token is not None and self.current_token.type == TokenType.NOR_BOOLEAN:
        self.advance()
        result = NorBooleanNode(result, self.factor())

    return result

  def factor(self):
    token = self.current_token

    if token.type == TokenType.CONDITIONAL:
      return self.conditionalExpr()

    if token.type == TokenType.ROUND:
      return self.roundExpr()

    if token.type == TokenType.SUM:
      return self.sumExpr()

    if token.type == TokenType.PRODUCT:
      return self.productExpr()

    if token.type == TokenType.MEAN:
      return self.meanExpr()

    if token.type == TokenType.MEDIAN:
      return self.medianExpr()

    if token.type == TokenType.MAX:
      return self.maxExpr()

    if token.type == TokenType.MIN:
      return self.minExpr()

    if token.type == TokenType.RANGE:
      return self.rangeExpr()

    if token.type == TokenType.MODE:
      return self.modeExpr()

    if token.type == TokenType.LPAREN:
      self.advance()
      result = self.expr()

      if self.current_token.type != TokenType.RPAREN:
        self.raise_error()

      self.advance()
      return result

    if token.type == TokenType.LBRACKET:
      return self.arrayExpr()

    if token.type == TokenType.PLUS:
      self.advance()
      return PlusNode(self.factor())

    if token.type == TokenType.MINUS:
      self.advance()
      return MinusNode(self.factor())

    if token.type == TokenType.NOT_BOOLEAN:
      self.advance()
      return NotBooleanNode(self.factor())

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

    if token.type == TokenType.CONDITIONAL:
      self.advance()
      return ConditionalNode(token.value)

    if token.type == TokenType.FUNCTION:
      self.advance()
      return FunctionNode(token.value)

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

    if token.type == TokenType.ERROR_WORDS:
      self.advance()
      return ErrorWordsNode(token.value)
    self.raise_error()

  def conditionalExpr(self):
    cases = []
    else_case = None

    # --- IF ---
    self.eat(TokenType.CONDITIONAL)   # eat IF
    condition = self.expr()
    self.eat(TokenType.COLON)
    expr_value = self.expr()
    cases.append((condition, expr_value))

    # --- ELIF(s) ---
    while self.current_token is not None and self.current_token.type == TokenType.ELIF:
      self.eat(TokenType.ELIF)
      condition = self.expr()
      self.eat(TokenType.COLON)
      expr_value = self.expr()
      cases.append((condition, expr_value))

    # --- ELSE (optional) ---
    if self.current_token is not None and self.current_token.type == TokenType.ELSE:
      self.eat(TokenType.ELSE)
      self.eat(TokenType.COLON)
      else_case = self.expr()

    # --- END (required) ---
    self.eat(TokenType.END)

    return ConditionalNode(cases, else_case)

  def roundExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      raise Exception("Error: round() expects '('")

    self.advance()

    value_node = self.expr()

    precision_node = None

    if self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      precision_node = self.expr()

    if self.current_token is None or self.current_token.type != TokenType.RPAREN:
      raise Exception("Error: round() expects ')'")

    self.advance()

    return RoundNode(value_node, precision_node)

  def sumExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return SumNode(values)

  def productExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return ProductNode(values)

  def meanExpr(self):
    self.advance()

    if self.current_token is None or self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()
    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      if self.current_token is None:
        self.raise_error()
      values.append(self.expr())

    if self.current_token is None or self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return MeanNode(values)

  def medianExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return MedianNode(values)

  def maxExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return MaxNode(values)

  def minExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return MinNode(values)

  def rangeExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
      self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
      self.advance()
      values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
      self.raise_error()

    self.advance()

    return RangeNode(values)

  def modeExpr(self):
    self.advance()

    if self.current_token.type != TokenType.LPAREN:
        self.raise_error()

    self.advance()

    values = []

    values.append(self.expr())

    while self.current_token is not None and self.current_token.type == TokenType.COMMA:
        self.advance()
        values.append(self.expr())

    if self.current_token.type != TokenType.RPAREN:
        self.raise_error()

    self.advance()

    return ModeNode(values)

  def arrayExpr(self):
    elements = []

    self.advance()

    if self.current_token.type == TokenType.RBRACKET:
      self.advance()
      return ArrayNode(elements)

    elements.append(self.expr())

    while self.current_token.type == TokenType.COMMA:
      self.advance()
      elements.append(self.expr())

    if self.current_token.type != TokenType.RBRACKET:
      self.raise_error("Expected ']'")

    self.advance()
    return ArrayNode(elements)

# Interpreter #

class Interpreter:
  def __init__(self):
    self.variables = {}
    self.functions = {}

  def visit(self, node):
    method_name = f'visit_{type(node).__name__}'
    method = getattr(self, method_name)
    return method(node)

  def visit_IntNode(self, node):
    return node.value

  def visit_FloatNode(self, node):
    return node.value

  def visit_AssignNode(self, node):
    # 1. Evaluate right-hand side
    value = self.visit(node.value)

    # 2. Enforce type
    if node.var_type == TokenType.NUMBER_VAR:
      if not isinstance(value, (int, float)):
        raise Exception(f"Type Error: value assigned to {node.name} must be a number")

    elif node.var_type == TokenType.STRING_VAR:
      if not isinstance(value, str):
        raise Exception(f"Type Error: value assigned to {node.name} must be a string")

    elif node.var_type == TokenType.ARRAY_VAR:
      if not isinstance(value, list):
        raise Exception(f"Type Error: value assigned to {node.name} must be a list")

    else:
      raise Exception("Invalid assignment target")

    # 3. Enforce immutability
    if node.name in self.variables:
      raise Exception(f"Type Error: variable '{node.name}' is immutable and cannot be reassigned")

    # 4. Store value
    self.variables[node.name] = value
    return None

  def visit_NumberSignNode(self, node):
    if node.value in important_numbers:
      return FloatNode(important_numbers[node.value])

    if node.value in self.variables:
      return self.variables[node.value]

    raise Exception(f"Error: Unknown numeric constant or variable '{node.value}'")

  def visit_StringSignNode(self, node):
    if node.value in self.variables:
      return self.variables[node.value]

    raise Exception(f"Error: Unknown string variable '{node.value}'")

  def visit_ArraySignNode(self, node):
    if node.value in self.variables:
        return self.variables[node.value]

    raise Exception(f"Error: Unknown array variable '{node.value}'")

  def visit_StringNode(self, node):
    return node.value

  def visit_ArrayNode(self, node):
    return [self.visit(el) for el in node.elements]

  def visit_PrintNode(self, node):
    var_name = node.var_name

    if var_name not in self.variables:
      raise Exception(f"Error: Undefined variable '{var_name}'")

    print(self.variables[var_name])
    return None

  def visit_ConditionalNode(self, node):
    for condition_node, expr_node in node.cases:
      if self.visit(condition_node) == True:
            return self.visit(expr_node)

    if node.else_case is not None:
      return self.visit(node.else_case)

    return None

  def visit_FunctionNode(self, node):
    self.functions[node.name] = node
    return None

  def visit_RoundNode(self, node):
    value_node = self.visit(node.value)

    if isinstance(value_node, (int, float)):
      value_node = FloatNode(value_node) if isinstance(value_node, float) else IntNode(value_node)

    if isinstance(value_node, IntNode):
      value = value_node.value
    elif isinstance(value_node, FloatNode):
      value = value_node.value
    else:
      raise Exception("Error: round() expects a numeric value")

    precision = 0
    if node.precision is not None:
      precision_node = self.visit(node.precision)
      if isinstance(precision_node, int):
        precision = precision_node
      elif isinstance(precision_node, IntNode):
        precision = precision_node.value
      else:
        raise Exception("Error: round() precision must be an integer")
      if precision < 0:
        raise Exception("Error: round() precision must be >= 0")

    factor = 10 ** precision
    shifted = value * factor

    if shifted >= 0:
      shifted_rounded = int(shifted + 0.5)
    else:
      shifted_rounded = int(shifted - 0.5)

    result = shifted_rounded / factor

    if precision == 0:
      return IntNode(int(result))
    else:
      return FloatNode(float(result))

  def visit_SumNode(self, node):
    values = []

    for expr in node.values:
      value = self.visit(expr)

      if isinstance(value, list):
        for item in value:
          if not isinstance(item, (int, float)):
            raise Exception("sum() requires numeric values")
          values.append(item)

      elif isinstance(value, (int, float)):
        values.append(value)

      else:
        raise Exception("sum() requires numeric values")

    if not values:
      raise Exception("sum() requires at least one value")

    result = sum(values)

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    elif isinstance(result, int):
      return IntNode(result)
    else:
      return FloatNode(result)

  def visit_ProductNode(self, node):
    values = []

    for expr in node.values:
      value = self.visit(expr)

      if isinstance(value, list):
        for item in value:
          if not isinstance(item, (int, float)):
            raise Exception("product() requires numeric values")
          values.append(item)

      elif isinstance(value, (int, float)):
        values.append(value)

      else:
        raise Exception("product() requires numeric values")

    if not values:
      raise Exception("product() requires at least one value")

    result = 1
    for v in values:
      result *= v

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    elif isinstance(result, int):
      return IntNode(result)
    else:
      return FloatNode(result)

  def visit_MeanNode(self, node):
    values = []

    for expr in node.values:
      value = self.visit(expr)

      if isinstance(value, list):
        for item in value:
          if not isinstance(item, (int, float)):
            raise Exception("mean() requires numeric values")
          values.append(item)

      elif isinstance(value, (int, float)):
        values.append(value)

      else:
        raise Exception("mean() requires numeric values")

    if not values:
      raise Exception("mean() requires at least one value")

    result = sum(values) / len(values)

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    else:
      return FloatNode(result)

  def visit_MedianNode(self, node):
    values = []

    for expr in node.values:
      value = self.visit(expr)

      if isinstance(value, list):
        for item in value:
          if not isinstance(item, (int, float)):
            raise Exception("median() requires numeric values")
          values.append(item)

      elif isinstance(value, (int, float)):
        values.append(value)

      else:
        raise Exception("median() requires numeric values")

    if not values:
      raise Exception("median() requires at least one value")

    values.sort()
    n = len(values)
    mid = n // 2

    if n % 2 == 1:
      median = values[mid]
    else:
      median = (values[mid - 1] + values[mid]) / 2

    if isinstance(median, float) and median.is_integer():
      return IntNode(int(median))
    elif isinstance(median, int):
      return IntNode(median)
    else:
      return FloatNode(median)

  def visit_MaxNode(self, node):
    values = []
    for expr in node.values:
      value = self.visit(expr)
      if isinstance(value, list):
        values.extend(value)
      else:
        values.append(value)

    for v in values:
      if not isinstance(v, (int, float)):
        raise Exception("max() requires numeric values")

    if not values:
      raise Exception("max() requires at least one value")

    max_value = max(values)

    if isinstance(max_value, float) and max_value.is_integer():
      return IntNode(int(max_value))
    elif isinstance(max_value, int):
      return IntNode(max_value)
    else:
      return FloatNode(max_value)

  def visit_MinNode(self, node):
    values = []
    for expr in node.values:
      value = self.visit(expr)
      if isinstance(value, list):
        values.extend(value)
      else:
        values.append(value)

    for v in values:
      if not isinstance(v, (int, float)):
        raise Exception("min() requires numeric values")

    if not values:
      raise Exception("min() requires at least one value")

    min_value = min(values)

    if isinstance(min_value, float) and min_value.is_integer():
      return IntNode(int(min_value))
    elif isinstance(min_value, int):
      return IntNode(min_value)
    else:
      return FloatNode(min_value)

  def visit_RangeNode(self, node):
    values = []
    for expr in node.values:
      value = self.visit(expr)
      if isinstance(value, list):
        values.extend(value)
      else:
        values.append(value)

    for v in values:
      if not isinstance(v, (int, float)):
        raise Exception("range() requires numeric values")

    if not values:
      raise Exception("range() requires at least one value")

    range_value = max(values) - min(values)

    if isinstance(range_value, float) and range_value.is_integer():
      return IntNode(int(range_value))
    elif isinstance(range_value, int):
      return IntNode(range_value)
    else:
      return FloatNode(range_value)

  def visit_ModeNode(self, node):
    values = []

    for expr in node.values:
      value_node = self.visit(expr)

      if isinstance(value_node, list):
        values.extend(value_node)
      else:
        values.append(value_node)

    for v in values:
      if not isinstance(v, (int, float)):
        raise Exception("mode() requires numeric values")

    if not values:
      raise Exception("mode() requires at least one value")

    frequency = {}
    for v in values:
      frequency[v] = frequency.get(v, 0) + 1

    max_count = max(frequency.values())

    modes = [k for k, v in frequency.items() if v == max_count]

    if len(modes) == len(frequency):
      raise Exception("mode() has no mode (all values occur equally)")

    if len(modes) == 1:
      return modes[0]
    else:
      return modes

  def visit_SquareNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("square() requires numeric input")

    result = value * value

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    elif isinstance(result, int):
      return IntNode(result)
    else:
      return FloatNode(result)

  def visit_SquareRootNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("sqrt() requires numeric input")

    if value < 0:
      raise Exception("sqrt() requires non-negative input")

    result = value ** 0.5

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    else:
      return FloatNode(result)

  def visit_AbsoluteValueNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("abs() requires numeric input")

    result = abs(value)

    if isinstance(result, float) and result.is_integer():
      return IntNode(int(result))
    elif isinstance(result, int):
      return IntNode(result)
    else:
      return FloatNode(result)

  def visit_CeilNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("ceil() requires numeric input")

    if isinstance(value, int):
      result = value
    else:
      if value.is_integer():
        result = int(value)
      elif value > 0:
        result = int(value) + 1
      else:
        result = int(value)

    return IntNode(result)

  def visit_FloorNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("floor() requires numeric input")

    if isinstance(value, int):
      result = value
    else:
      if value.is_integer():
        result = int(value)
      elif value > 0:
        result = int(value)
      else:
        result = int(value) - 1

    return IntNode(result)

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

  def visit_EqualNode(self, node):
    check_x = self.visit(node.node_x)
    check_y = self.visit(node.node_y)

    # Allow number == number
    if isinstance(check_x, (int, float)) and isinstance(check_y, (int, float)):
      return check_x == check_y

    # Allow string == string
    if isinstance(check_x, str) and isinstance(check_y, str):
      return check_x == check_y

    # Allow boolean == boolean (optional but nice)
    if isinstance(check_x, bool) and isinstance(check_y, bool):
      return check_x == check_y

    # Different types are never equal
    return False

  def visit_GreaterThanNode(self, node):
    check_x = self.visit(node.node_x)
    check_y = self.visit(node.node_y)

    if not isinstance(check_x, (int, float)) or not isinstance(check_y, (int, float)):
      raise Exception("GreaterThanNode requires numeric values")

    return check_x > check_y

  def visit_LessThanNode(self, node):
    check_x = self.visit(node.node_x)
    check_y = self.visit(node.node_y)

    if not isinstance(check_x, (int, float)) or not isinstance(check_y, (int, float)):
      raise Exception("LessThanNode requires numeric values")

    return check_x < check_y

  def visit_GreaterThanEqualNode(self, node):
    check_x = self.visit(node.node_x)
    check_y = self.visit(node.node_y)

    if not isinstance(check_x, (int, float)) or not isinstance(check_y, (int, float)):
      raise Exception("GreaterThanEqualNode requires numeric values")

    return check_x >= check_y

  def visit_LessThanEqualNode(self, node):
    check_x = self.visit(node.node_x)
    check_y = self.visit(node.node_y)

    if not isinstance(check_x, (int, float)) or not isinstance(check_y, (int, float)):
        raise Exception("LessThanEqualNode requires numeric values")

    return check_x <= check_y

  def visit_NotEqualNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    # number != number
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
      return left != right

    # string != string
    if isinstance(left, str) and isinstance(right, str):
      return left != right

    # boolean != boolean (optional but consistent)
    if isinstance(left, bool) and isinstance(right, bool):
      return left != right

    # different types are always not equal
    return True

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
    value_a = self.visit(node.node_a)
    value_b = self.visit(node.node_b)

    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
      raise Exception("Addition requires numeric inputs")

    result = value_a + value_b

    if isinstance(result, float) and result.is_integer():
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

  def visit_SubtractNode(self, node):
    value_a = self.visit(node.node_a)
    value_b = self.visit(node.node_b)

    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
      raise Exception("Subtraction requires numeric inputs")

    result = value_a - value_b

    if isinstance(result, float) and result.is_integer():
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

  def visit_MultiplyNode(self, node):
    value_a = self.visit(node.node_a)
    value_b = self.visit(node.node_b)

    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
      raise Exception("Multiplication requires numeric inputs")

    result = value_a * value_b

    if isinstance(result, float) and result.is_integer():
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

  def visit_DivideNode(self, node):
    value_a = self.visit(node.node_a)
    value_b = self.visit(node.node_b)

    if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
      raise Exception("Division requires numeric inputs")

    if value_b == 0:
      raise Exception("Division by zero")

    quotient = value_a / value_b

    if isinstance(quotient, float) and quotient.is_integer():
      return int(quotient)
    elif isinstance(quotient, int):
      return quotient
    elif isinstance(quotient, float):
      return quotient

  def visit_PlusNode(self, node):
    return self.visit(node.node)

  def visit_MinusNode(self, node):
    check_num = self.visit(node.node)

    if not isinstance(check_num, (int, float)):
      raise Exception("Minus requires a numeric value")

    return -check_num

  def visit_NumberTypeNode(self, node):
    value = self.visit(node.node)

    return isinstance(value, (int, float))

  def visit_IntegerTypeNode(self, node):
    value = self.visit(node.node)

    if isinstance(value, int):
      return True

    if isinstance(value, float) and value.is_integer():
      return True

    return False

  def visit_FloatTypeNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
        return False

    if isinstance(value, float) and not value.is_integer():
        return True

    return False

  def visit_EvenCheckNode(self, node):
    value = self.visit(node.node)

    if isinstance(value, float) and value.is_integer():
      value = int(value)

    if isinstance(value, int):
      return value % 2 == 0

    return False

  def visit_OddCheckNode(self, node):
    value = self.visit(node.node)

    if isinstance(value, float) and value.is_integer():
      value = int(value)

    if isinstance(value, int):
      return value % 2 != 0

    return False

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
    value = self.visit(node.node)

    return isinstance(value, str)

  def visit_AndBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    if isinstance(left, BooleanNode):
      left = left.value
    if isinstance(right, BooleanNode):
      right = right.value

    result = bool(left) and bool(right)
    return BooleanNode(result)

  def visit_NandBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    if isinstance(left, BooleanNode):
        left = left.value
    if isinstance(right, BooleanNode):
        right = right.value

    result = not (bool(left) and bool(right))
    return BooleanNode(result)

  def visit_OrBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    if isinstance(left, BooleanNode):
      left = left.value
    if isinstance(right, BooleanNode):
      right = right.value

    result = bool(left) or bool(right)
    return BooleanNode(result)

  def visit_XorBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    if isinstance(left, BooleanNode):
      left = left.value
    if isinstance(right, BooleanNode):
      right = right.value

    result = bool(left) != bool(right)
    return BooleanNode(result)

  def visit_NorBooleanNode(self, node):
    left_node = self.visit(node.node_x)
    right_node = self.visit(node.node_y)

    left_val = left_node.value
    right_val = right_node.value

    result = not (left_val or right_val)
    return BooleanNode(result)

  def visit_NotBooleanNode(self, node):
    inner = self.visit(node.node)

    if isinstance(inner, BooleanNode):
      value = inner.value
    else:
      value = inner

    return BooleanNode(not bool(value))

  def visit_BooleanNode(self, node):
    value = node.value
    if not isinstance(value, bool):
      value = self.visit(value)
    return BooleanNode(bool(value))

  def visit_ErrorWordsNode(self, node):
    raise Exception(f"Unknown identifier '{node.value}'")

class PrintNode:
  def __init__(self, var_name):
    self.var_name = var_name

# Run #

interpreter = Interpreter()

while True:
  text = input("Enter a math function: ")
  lexer = Lexer(text)
  tokens = list(lexer.generate_tokens())
  parser = Parser(tokens)
  tree = parser.parse()
  if tree is None: continue
  print(tree)
  value = interpreter.visit(tree)
  if isinstance(tree, (NumberSignNode, StringSignNode, ArraySignNode)):
    continue
  if value is not None:
    print(value)