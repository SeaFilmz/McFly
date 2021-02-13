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