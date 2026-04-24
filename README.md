# McFly
It learns from the past but looks to the future, McFly.

## What is McFly?

![McFly running in Windows Powershell](.github/mcfly.gif)

McFly coding language is a math- and statistics-focused programmable calculator being developed in Python.


## The components of McFly:

### Arithmetic Operators 
  
- `+` for addition.
- `-` for subtraction.
- `*` for multiplication.
- `/` for division.
- `^` for exponent.


### Math Functions

- `square` returns the square of a numeric value.
- `sqrt` returns the square root of a numeric value.
- `abs()` returns the absolute (non-negative) value of numeric input. It supports a single number, multiple numbers, a number variable, or a list (including list variables). When give multiple values or a list, the function applies to each item individually.
- `ceil` rounds a numeric value up to the nearest integer.
- `floor` rounds a numeric value down to the nearest integer.
- `round()` rounds a numeric value to the specified number of decimal places (default is 0) using standard rounding rules: 
  - next digit 0–4 rounds down
  - next digit 5–9 rounds up
- `sum()` returns the sum of all numeric inputs.
- `product()` returns the product (multiplication result) of all numeric inputs.


### Statistics Functions

- `count()` returns the number of items in a list.
- `mean()` returns the average of the given numeric values.
- `median()` returns the middle value of the given numeric values when they are sorted.
- `mode()` returns the value or values that appear most frequently in the given numeric values.
- `max()` returns the largest numeric value from the given inputs.
- `min()` returns the smallest numeric value from the given inputs.
- `range()` returns the difference between the maximum and minimum values of the given inputs.


### Comparison Operations 
  
- `==` for comparing if 2 values are equal. Works with numbers, strings and boolean values.
- `>` for comparing if 1 number is greater than another number.
- `<` for comparing if 1 number is less than another number.
- `>=` for comparing if 1 number is greater than another number or has the same numerical value.
- `<=` for comparing if 1 number is less than another number or has the same numerical value.
- `!=` for comparing if 2 numbers do not have the same numerical value.


### Boolean Operations
  
- `and` checks if both values are `True`. If so, then it will output `True`, else it will output `False`.
- `nand` is the opposite of `and`. `nand` is checks if 0 or 1 values is `True`. If so, then it will output `True`, else it will output `False`.
- `or` checks if at least 1 or 2 values is `True`. If so, then it will output `True`, else it will output `False`.
- `xor` checks if 1 of 2 values is `True`. If so then it will output `True` else it will output `False`.
- `nor` is the opposite of `or`. `nor` checks for if both values are `False` if so then it will output `True`, else it will output `False`.
- `not` inverts the output of the boolean values `True` or `False`.


### Type / Checker Operators

- `num?` checks if a value is a number (integer or float).
- `intNum?` checks if a number is an integer based on math rules (whole numbers, including values like 3.0).
- `intType?` checks if a value is stored as an integer type.
- `float?` checks if a value is stored as a float.
- `even?` checks if a number is even.
- `odd?` checks if a number is odd.
- `positive?` checks if a number is positive (>0).
- `negative?` checks if a number is negative (<0).
- `str?` checks if a value is a string.
- `zero?` checks if a number is equal to 0 using math rules.
- `list?` checks whether a value is of type list.
  
  
### String Command
- `"` is used at the beginning and end of text to convert it to a string. 
>💡 The string output is printed without including the beginning and ending quotation marks.


### Immutable Variables

Variables in this language are immutable, meaning they can only be assigned once and cannot be reassigned.
- Number variable names start with `#` and can store integers or floating-point values.
- String variable names start with `$` and can store text values.
- List variable names start with `@` and can store ordered collections of values.


### Constants
  
- `#pi` is equal to `3.141592653589793`
- `#tau` is equal to `6.283185307179586`
- `#e` is equal to `2.718281828459045`


### Conditionals

Conditionals evaluate logic and return a value from the first true branch.
- `if` checks the first condition.
- `elif` checks another condition if previous ones were false.
- `else` fallback value if no conditions are true.
- `end` marks the official conclusion of the conditional block.


### User-Defined Functions

User-Defined Functions are immutable blocks of reusable logic.
- `fun` declares the beginning of a new function.
- `:` marks the transition from the function name to its code.
- `end` signals the official end of the function block.


### Comments

- `/~` is for single-line comments which allow you to add a note after it on the same line that are ignored during execution.



## Examples:
- Input: `3+3-3*3/3` Outputs: `3`
- Input: `#pi` Outputs: `3.141592653589793` 
- Input: `3+#pi*2` Outputs: `9.283185307179586`
- Input: `3.0==3` Outputs: `True`
- Input: `3.14==3.5` Outputs: `False`
- Input: `3.0===3` Outputs: `False`
- Input: `True or True` Outputs: `True`
- Input: `"Hello World!"` Outputs: `Hello World!`


## Upcoming Features:


## Optimizations:  

## How to run McFly on Windows:

1. Open Terminal by pressing Windows Key + X on your keyboard. In the menu that appears, click on Terminal (it may also be listed as Windows PowerShell or Command Prompt).
1. In the terminal type python3 --version and press Enter. If you see Python 3.7.x (or any version higher than 3.7), skip to Step 4. If python3 gives an error, try typing python --version instead. If you see a version lower than 3.7.x or get an error for both, you must install the latest version of Python 3 in Step 3.
1. [Install Python version 3 or higher.](https://www.python.org/downloads/) (If you already have version 3 or higher of Python installed you may omit this step.)
1. Create a folder called mcfly.
1. [Navigate to the raw mcfly.py file on GitHub.]("https://raw.githubusercontent.com/SeaFilmz/McFly/DevCode/mcfly.py")
1. At the top right of the code view click Download raw file.
1. Save that file in the mcfly folder as mcfly.py.
1. Use Windows Explorer to navigate to the mcfly folder (make sure that folder has a mcfly.py file)

### Steps for Running the External File Version

9. [Install VS Code.](https://code.visualstudio.com/) (If you already have VS Code installed you may omit this step.)
10. Open VS Code.
11. Go to file menu and click on Open Folder...
12. Find your mcfly folder and open it.
13. Go to the top left side and click on the Explorer tab.
14. In that tab right click and select New File... from that menu.
15. Type the name of file with the extension `.mcfly` (example: `test.mcfly`) and press Enter.
16. Write your McFly code in that file.
18. Open Terminal pressing Ctrl + Shift + ` keys.
19. At the botton below your code a box opened. Make sure your in the TERMINAL tab of that box. In that tab type `python3 mcfly.py test.mcfly` and press Enter. You should see the results of your code populate in that box. If the results did not populate in the box try typing python mcfly.py test.mcfly instead.

### Steps for Running the REPL Version

9.  Do Step 1.
10. Type cd and a space.
11. Find your mcfly folder.
12. Drag and Drop that folder into the terminal.
13. Press Enter. You should now seen the address path to your mclfy folder in the terminal.
14. Type `python3 mcfly.py` and press Enter. If your terminal displays `Enter McFly Code:` then Mcfly is running. If it did not display `Enter McFly Code:` then type `python mcfly.py` and press Enter.
15. Write your McFly code in the terminal. 
16. To run that McFly code you wrote press Enter.
