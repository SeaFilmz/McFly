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

- User-Defined Functions 

  
## Optimizations:  

## How to run McFly on Windows:

1. [Install Python version 3 or higher.](https://www.python.org/downloads/) (If you already have version 3 or higher of Python installed you may omit this step.)
1. Create a folder called mcfly.
1. [Navigate to the raw mcfly.py file on GitHub.]("https://raw.githubusercontent.com/SeaFilmz/McFly/DevCode/mcfly.py")
1. Right click on the page and click `Save As...`
1. Save that file in the mcfly folder as mcfly.py.
1. Use Windows Explorer to navigate to the mcfly folder (make sure that folder has a mcfly.py file)

### Steps for Running the External File Version
7. In the mcfly folder create a file with the extension `.mcfly` (example: `test.mcfly`).
8. Open the `.mcfly` file in a text editor.
9. Write your McFly code in that file.
10. Save the McFly code in that file.
11. Go back to the McFly folder.
12. Click the Explorer Address Bar to highlight the current folder path.
13. Delete the text, type `powershell`, and press Enter.
14. Powershell will open in the same directory you have navigated to. 
15. While in Powershell, run the command `python mcfly.py test.mcfly`.
16. You should now see the execution of your `.mcfly` file in the terminal.

### Steps for Running the REPL Version

7. Click into the Explorer Address Bar to highlight the text.
8. Delete the text, type `powershell` in the Address Bar, press enter.
9. Powershell will open in the same directory you have navigated to.
10. While in Powershell, run the command `python mcfly.py`. 
11. McFly is running and ready to use if your terminal displays `Enter McFly Code:`

>💡 If you close powershell, you will need to repeat instructions 6-9 to rerun McFly.
 
