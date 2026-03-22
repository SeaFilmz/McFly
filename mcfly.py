from enum import Enum, auto
from dataclasses import dataclass
import sys

# Dictionary #

important_numbers = {
  '#pi': 3.141592653589793,
  '#tau': 6.283185307179586,
  '#e': 2.718281828459045
}

custom_strings = {}

custom_lists = {}

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
  EXPONENT       = auto()
  LPAREN         = auto()
  RPAREN         = auto()
  LBRACKET       = auto()
  RBRACKET       = auto()
  COMMA          = auto()
  ASSIGN         = auto()
  NUMBER_VAR     = auto()
  STRING_VAR     = auto()
  LIST_VAR       = auto()
  GT             = auto()
  LT             = auto()
  GTE            = auto()
  LTE            = auto()
  NE             = auto()
  EQUALS         = auto()
  STRING         = auto()
  NUMBER_TYPE    = auto()
  INTEGER_NUMBER = auto()
  INTEGER_TYPE   = auto()
  FLOAT_TYPE     = auto()
  STRING_TYPE    = auto()
  LIST_TYPE      = auto()
  EVEN_CHECK     = auto()
  ODD_CHECK      = auto()
  POSITIVE_CHECK = auto()
  NEGATIVE_CHECK = auto()
  ZERO_CHECK     = auto()
  AND_BOOLEAN    = auto()
  NAND_BOOLEAN   = auto()
  OR_BOOLEAN     = auto()
  XOR_BOOLEAN    = auto()
  NOR_BOOLEAN    = auto()
  NOT_BOOLEAN    = auto()
  TRUE           = auto()
  FALSE          = auto()
  IDENTIFIER     = auto()
  FUNCTION       = auto()
  CONDITIONAL    = auto()
  ELSE           = auto()
  ELIF           = auto()
  COLON          = auto()
  END            = auto()
  COUNT          = auto()
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
  COMMENT        = auto()
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
    while self.current_char is not None:
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
        yield self.generate_list_var()
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
        token = self.generate_front_slash_action()
        if token is not None:
          yield token
      elif self.current_char == '^':
        self.advance()
        yield Token(TokenType.EXPONENT)
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
        elif upper_word == "INTNUM?":
          yield Token(TokenType.INTEGER_NUMBER)
        elif upper_word == "INTTYPE?":
          yield Token(TokenType.INTEGER_TYPE)
        elif upper_word == "FLOAT?":
          yield Token(TokenType.FLOAT_TYPE)
        elif upper_word == "STR?":
          yield Token(TokenType.STRING_TYPE)
        elif upper_word == "LIST?":
          yield Token(TokenType.LIST_TYPE)
        elif upper_word == "ODD?":
          yield Token(TokenType.ODD_CHECK)
        elif upper_word == "EVEN?":
          yield Token(TokenType.EVEN_CHECK)
        elif upper_word == "POSITIVE?":
          yield Token(TokenType.POSITIVE_CHECK)
        elif upper_word == "NEGATIVE?":
          yield Token(TokenType.NEGATIVE_CHECK)
        elif upper_word == "ZERO?":
          yield Token(TokenType.ZERO_CHECK)
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
        elif upper_word == "COUNT":
          yield Token(TokenType.COUNT)
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
          yield Token(TokenType.IDENTIFIER, word)
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

  def generate_list_var(self):
    if not self.current_char.isalpha():
      raise Exception("List variable must start with a letter after '@'")

    var_name = "@" + self.current_char
    self.advance()

    while (
      self.current_char is not None and
      (self.current_char.isalnum() or self.current_char == "_")
    ):
      var_name += self.current_char
      self.advance()

    return Token(TokenType.LIST_VAR, var_name)

  def generate_equals(self):
    self.advance()

    if self.current_char == '=':
      self.advance()
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
      return Token(TokenType.NE)

  def generate_front_slash_action(self):
    # Check the next character safely
    next_char = self.text[self.pos + 1] if self.pos + 1 < len(self.text) else None

    # If "/-" → single-line comment
    if next_char == '~':
        self.advance()  # consume '/'
        self.advance()  # consume '-'

        # Skip everything until newline
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

        # Skip the newline itself
        if self.current_char == '\n':
            self.advance()

        return None  # comment produces no token

    # Otherwise it's division
    self.advance()
    return Token(TokenType.DIVIDE)

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
class ListNode:
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
class ExponentNode:
  node_a: any
  node_b: any

  def __repr__(self):
    return f"({self.node_a}^{self.node_b})"

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
class ListSignNode:
  value: str

  def __repr__(self):
    return f"{self.value}"

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
class ChainCompareNode:
  values: list
  operators: list[str]

  def __repr__(self):
    result = str(self.values[0])
    for i, op in enumerate(self.operators):
      result += f" {op} {self.values[i+1]}"
    return result

@dataclass
class NumberTypeNode:
  node: any

  def __repr__(self):
    return f"(num?{self.node})"

@dataclass
class IntegerTypeNode:
  node: any

  def __repr__(self):
    return f"(intType?{self.node})"

@dataclass
class IntegerCheckNode:
  node: any

  def __repr__(self):
    return f"(intNum?{self.node})"

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
class ZeroCheckNode:
  node: any

  def __repr__(self):
    return f"(zero?{self.node})"

@dataclass
class StringTypeNode:
  node: any

  def __repr__(self):
    return f"(str?{self.node})"

@dataclass
class ListTypeNode:
  node: any

  def __repr__(self):
    return f"(list?{self.node})"

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
class CountNode:
  values: list

  def __repr__(self):
    valuesList = ", ".join(map(str, self.values))
    return f"count({valuesList})"

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
  node: list

  def __repr__(self):
    return f"square {self.node}"

@dataclass
class SquareRootNode:
  node: list

  def __repr__(self):
    return f"sqrt {self.node}"

@dataclass
class AbsoluteValueNode:
  node: list

  def __repr__(self):
    return f"abs {self.node}"

@dataclass
class CeilNode:
  node: list

  def __repr__(self):
    return f"(ceil{self.node})"

@dataclass
class FloorNode:
  node: list

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
    body = self.conditional()

    return FunctionNode(name, params, body)

  def conditional(self):
    cases = []
    else_case = None

    # --- IF ---
    self.eat(TokenType.CONDITIONAL)   # eat IF
    condition = self.orCheck()
    self.eat(TokenType.COLON)
    expr_value = self.statement()
    cases.append((condition, expr_value))

    # --- ELIF(s) ---
    while self.current_token is not None and self.current_token.type == TokenType.ELIF:
      self.eat(TokenType.ELIF)
      condition = self.orCheck()
      self.eat(TokenType.COLON)
      expr_value = self.statement()
      cases.append((condition, expr_value))

    # --- ELSE (optional) ---
    if self.current_token is not None and self.current_token.type == TokenType.ELSE:
      self.eat(TokenType.ELSE)
      self.eat(TokenType.COLON)
      else_case = self.statement()

    # --- END (required) ---
    self.eat(TokenType.END)

    return ConditionalNode(cases, else_case)

  def statement(self):
    if self.current_token.type == TokenType.CONDITIONAL:
      return self.conditional()

    if self.current_token.type == TokenType.PRINT:
      return self.print_statement()

    if (self.current_token.type in (
      TokenType.NUMBER_VAR,
      TokenType.STRING_VAR,
      TokenType.LIST_VAR,
    ) and self.peek() is not None and self.peek().type == TokenType.ASSIGN):
      return self.assignment()

    return self.orCheck()

  def print_statement(self):
    self.expect(TokenType.PRINT)

    token = self.current_token

    if token.type not in (
      TokenType.NUMBER_VAR,
      TokenType.STRING_VAR,
      TokenType.LIST_VAR,
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

    value = self.orCheck()

    return AssignNode(var_token.type, name, value)

  def orCheck(self):
    result = self.xorCheck()

    while self.current_token is not None and self.current_token.type in (TokenType.OR_BOOLEAN, TokenType.NOR_BOOLEAN):
        token = self.current_token
        self.advance()

        right = self.xorCheck()

        if token.type == TokenType.OR_BOOLEAN:
            result = OrBooleanNode(result, right)
        else:
            result = NorBooleanNode(result, right)

    return result

  def xorCheck(self):
    result = self.andCheck()

    while self.current_token is not None and self.current_token.type == TokenType.XOR_BOOLEAN:
      self.advance()
      result = XorBooleanNode(result, self.andCheck())

    return result

  def andCheck(self):
    result = self.notCheck()

    while self.current_token is not None and self.current_token.type in (TokenType.AND_BOOLEAN, TokenType.NAND_BOOLEAN):
      token = self.current_token
      self.advance()

      right = self.notCheck()

      if token.type == TokenType.AND_BOOLEAN:
        result = AndBooleanNode(result, right)
      else:
        result = NandBooleanNode(result, right)

    return result

  def notCheck(self):
    if self.current_token is not None and self.current_token.type == TokenType.NOT_BOOLEAN:
        self.advance()
        return NotBooleanNode(self.notCheck())  # recursive for multiple nots

    return self.comparisonCheck()

  def comparisonCheck(self):
    values = [self.expr()]
    operators = []

    while self.current_token is not None and self.current_token.type in (
      TokenType.LT,
      TokenType.LTE,
      TokenType.GT,
      TokenType.GTE,
      TokenType.EQUALS,
      TokenType.NE,
    ):
      op = self.current_token.type
      self.advance()

      operators.append(op)
      values.append(self.expr())

    if not operators:
      return values[0]

    return ChainCompareNode(values, operators)

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
    result = self.exponent()

    while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.exponent())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.exponent())

    return result

  def exponent(self):
    left = self.factor()

    if self.current_token is not None and self.current_token.type == TokenType.EXPONENT:
      self.advance()
      right = self.exponent()
      return ExponentNode(left, right)

    return left

  def factor(self):
    token = self.current_token

    if token.type == TokenType.ABSOLUTE_VALUE:
      return self.absoluteValueExpr()

    if token.type == TokenType.ROUND:
      return self.roundExpr()

    if token.type == TokenType.COUNT:
      return self.countExpr()

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
      return self.listExpr()

    if token.type == TokenType.PLUS:
      self.advance()
      return PlusNode(self.factor())

    if token.type == TokenType.MINUS:
      self.advance()
      return MinusNode(self.factor())

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

    if token.type == TokenType.FUNCTION:
      self.advance()
      return FunctionNode(token.value)

    if token.type == TokenType.NUMBER_TYPE:
      self.advance()
      return NumberTypeNode(self.factor())

    if token.type == TokenType.INTEGER_TYPE:
      self.advance()
      return IntegerTypeNode(self.factor())

    if token.type == TokenType.INTEGER_NUMBER:
      self.advance()
      return IntegerCheckNode(self.factor())

    if token.type == TokenType.FLOAT_TYPE:
      self.advance()
      return FloatTypeNode(self.factor())

    if token.type == TokenType.STRING_TYPE:
      self.advance()
      return StringTypeNode(self.factor())

    if token.type == TokenType.LIST_TYPE:
      self.advance()
      return ListTypeNode(self.factor())

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

    if token.type == TokenType.ZERO_CHECK:
      self.advance()
      return ZeroCheckNode(self.factor())

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

    if token.type == TokenType.LIST_VAR:
      self.advance()
      return ListSignNode(token.value)

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

  def absoluteValueExpr(self):
    self.expect(TokenType.ABSOLUTE_VALUE)

    # Require parentheses
    self.expect(TokenType.LPAREN)

    args = []

    # If not empty
    if self.current_token.type != TokenType.RPAREN:
      args.append(self.expr())

      while self.current_token.type == TokenType.COMMA:
        self.advance()
        args.append(self.expr())

    self.expect(TokenType.RPAREN)

    return AbsoluteValueNode(args)

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

  def countExpr(self):
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

    return CountNode(values)

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

  def listExpr(self):
    elements = []

    self.advance()

    if self.current_token.type == TokenType.RBRACKET:
      self.advance()
      return ListNode(elements)

    elements.append(self.expr())

    while self.current_token.type == TokenType.COMMA:
      self.advance()
      elements.append(self.expr())

    if self.current_token.type != TokenType.RBRACKET:
      self.raise_error("Expected ']'")

    self.advance()
    return ListNode(elements)

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
        print()
        raise Exception(f'Type Error: {node.name} must be assigned a number. Change "{value}" from {type(value).__name__} to a number.')

    elif node.var_type == TokenType.STRING_VAR:
      if not isinstance(value, str):
        raise Exception(f'Type Error: {node.name} must be assigned a string. Change "{value}" from {type(value).__name__} to a string.')

    elif node.var_type == TokenType.LIST_VAR:
      if not isinstance(value, list):
        raise Exception(f'Type Error: {node.name} must be assigned a list. Change "{value}" from {type(value).__name__} to a list.')

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
      return important_numbers[node.value]

    if node.value in self.variables:
      return self.variables[node.value]

    raise Exception(f"Syntax Error: Numeric variable name contains invalid character(s). Remove invalid character(s) from the numeric variable name or change it to valid character(s).")

  def visit_StringSignNode(self, node):
    if node.value in self.variables:
      return self.variables[node.value]

    raise Exception(f"Syntax Error: String variable name contains invalid character(s). Remove invalid character(s) from the string variable name or change it to valid character(s).")

  def visit_ListSignNode(self, node):
    if node.value in self.variables:
        return self.variables[node.value]

    raise Exception(f"Syntax Error: List variable name contains invalid character(s). Remove invalid character(s) from the list variable name or change it to valid character(s).")

  def visit_StringNode(self, node):
    return node.value

  def visit_ListNode(self, node):
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
    value = self.visit(node.value)

    if not isinstance(value, (int, float)):
        raise Exception("Error: round() expects a numeric value")

    precision = 0

    if node.precision is not None:
      precision_value = self.visit(node.precision)

      if not isinstance(precision_value, int):
        raise Exception("Error: round() precision must be an integer")

      if precision_value < 0:
        raise Exception("Error: round() precision must be >= 0")

      precision = precision_value

    factor = 10 ** precision
    shifted = value * factor

    if shifted >= 0:
      shifted_rounded = int(shifted + 0.5)
    else:
      shifted_rounded = int(shifted - 0.5)

    result = shifted_rounded / factor

    if precision == 0:
      return int(result)
    else:
      return float(result)

  def visit_CountNode(self, node):
    value = self.visit(node.values[0])

    if isinstance(value, list):
      return len(value)

    raise Exception(f'Type Error: count() only accepts lists but got {type(value).__name__}. Change "{value}" from {type(value).__name__} to a list.')

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
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

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
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

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
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

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
      return int(median)
    elif isinstance(median, int):
      return median
    elif isinstance(median, float):
      return median

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
      return int(max_value)
    elif isinstance(max_value, int):
      return max_value
    elif isinstance(max_value, float):
      return max_value

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
      return int(min_value)
    elif isinstance(min_value, int):
      return min_value
    elif isinstance(min_value, float):
      return min_value

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
      return int(range_value)
    elif isinstance(range_value, int):
      return range_value
    elif isinstance(range_value, float):
      return range_value

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
      return int(result)
    else:
      return result

  def visit_SquareRootNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      raise Exception("sqrt() requires numeric input")

    if value < 0:
      raise Exception("sqrt() requires non-negative input")

    result = value ** 0.5

    if isinstance(result, float) and result.is_integer():
      return int(result)
    else:
      return result

  def visit_AbsoluteValueNode(self, node):

    def apply_abs(value):
      if isinstance(value, (int, float)):
        return abs(value)

      if isinstance(value, list):
        return [apply_abs(v) for v in value]

      raise Exception("abs() requires numeric input")

    results = []

    for arg in node.node:
      value = self.visit(arg)
      results.append(apply_abs(value))

    if len(results) == 1:
      return results[0]

    return results

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

    return result

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

    return result

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

  def visit_ChainCompareNode(self, node):
    left = self.visit(node.values[0])

    for i, op in enumerate(node.operators):
      right = self.visit(node.values[i + 1])

      if op == TokenType.LT:
        result = left < right
      elif op == TokenType.LTE:
        result = left <= right
      elif op == TokenType.GT:
        result = left > right
      elif op == TokenType.GTE:
        result = left >= right
      elif op == TokenType.EQUALS:
        result = left == right
      elif op == TokenType.NE:
        result = left != right
      else:
        raise Exception(f"Unknown operator {op}")

      if not result:
        return False

      left = right

    return True

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

  def visit_ExponentNode(self, node):
    base = self.visit(node.node_a)
    exponent = self.visit(node.node_b)

    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
      raise Exception("Exponentiation requires numeric inputs")

    result = base ** exponent

    if isinstance(result, float) and result.is_integer():
      return int(result)
    elif isinstance(result, int):
      return result
    elif isinstance(result, float):
      return result

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

    return False

  def visit_IntegerCheckNode(self, node):
    value = self.visit(node.node)

    if isinstance(value, int):
      return True

    if isinstance(value, float) and value.is_integer():
      return True

    return False

  def visit_FloatTypeNode(self, node):
    value = self.visit(node.node)

    if isinstance(value, float):
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
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      return False

    return value > 0

  def visit_NegativeCheckNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
        return False

    return value < 0

  def visit_ZeroCheckNode(self, node):
    value = self.visit(node.node)

    if not isinstance(value, (int, float)):
      return False

    return value == 0

  def visit_StringTypeNode(self, node):
    value = self.visit(node.node)

    return isinstance(value, str)

  def visit_ListTypeNode(self, node):
    value = self.visit(node.node)

    return isinstance(value, list)

  def visit_AndBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    return bool(left) and bool(right)

  def visit_NandBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    return not (bool(left) and bool(right))

  def visit_OrBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    return bool(left) or bool(right)

  def visit_XorBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    return bool(left) != bool(right)

  def visit_NorBooleanNode(self, node):
    left = self.visit(node.node_x)
    right = self.visit(node.node_y)

    return not (bool(left) or bool(right))

  def visit_NotBooleanNode(self, node):
    value = self.visit(node.node)

    return not bool(value)

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

def run_text(text, interpreter):
    lexer = Lexer(text)
    tokens = list(lexer.generate_tokens())

    parser = Parser(tokens)
    tree = parser.parse()

    if tree is None:
        return

    print(tree)

    value = interpreter.visit(tree)

    if isinstance(tree, (NumberSignNode, StringSignNode, ListSignNode)):
        return

    if value is not None:
        print(value)

def run_file(filename, interpreter):

  # Ensure the file uses the .McFly extension
  if not filename.endswith(".mcfly"):
    print("Error: McFly files must use the .mcfly extension")
    return

  try:
    with open(filename, "r") as file:
      for line in file:

        # Skip blank lines
        if line.strip() == "":
          continue

        # Skip single line comments
        if line.strip().startswith("/~"):
          continue

        run_text(line, interpreter)

  except FileNotFoundError:
    print(f"File not found: {filename}")

  except Exception as e:
    print("Error:", e)


if __name__ == '__main__':

  interpreter = Interpreter()

  # If a file is provided
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    run_file(filename, interpreter)

  # Otherwise start REPL
  else:
    while True:
      text = input("Enter McFly Code:")

      if text.strip().lower() == "exit":
        break

      run_text(text, interpreter)