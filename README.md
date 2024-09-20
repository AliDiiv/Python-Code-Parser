# 🐍 Python Code Parser

This Python script is designed to parse and interpret Python-like code from a file. It evaluates mathematical expressions, handles variable assignments, loops, conditionals, and produces output based on the parsed code. The main focus is on variable management and arithmetic operations.

## ✨ Features

- **Variable Assignment**: Supports variable assignments and simple operations.
- **Conditionals (`if-else`)**: Evaluates conditional statements with equality (`==`) and inequality (`!=`) comparisons.
- **Loops (`for` loop)**: Supports `for` loops using the `range()` function, allowing for arithmetic operations or output inside the loop.
- **Mathematical Operations**: Performs addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`) on variables or numbers.
- **Output Handling**: Supports printing variable values or text strings.

## ⚙️ How It Works

1. **File Input**: The script reads Python-like code from a file named `pycode.txt` located in the parent directory.
2. **Token Parsing**: The script processes lines of code, extracting keywords, variables, and operators, and executes them step by step.
3. **Mathematical Evaluation**: The `doMath()` function is used for handling arithmetic between variables or literals.
4. **Conditionals & Loops**: Supports `if-else` conditions and basic `for` loops for control flow.

## 📝 Example Code (`pycode.txt`)

Below is an example of Python-like code that the script can process:

```python
a = 5
b = 10
if a == b:
    print "Equal"
else:
    print "Not equal"

for i in range 3:
    print "Looping"
```
## 🖥️ Output

- The output of the script is printed to the console and includes the results of any print statements and variable evaluations.

## 🚀 How to Use

1. Place your Python-like code in a file named pycode.txt in the parent directory of the script. directory.
2. Run the script:
```python your_script_name.py
```
3. The output will be displayed in the console.

## 🔧 Customization

1. Max Variables: Modify the maximum number of variables by changing the max_vars value.
2. Tab Spaces: Adjust the number of spaces considered for indentation using the tab_spaces variable.

## ⚠️ Error Handling

The script provides error messages for:

1. Undefined variables in expressions.
2. Invalid comparison operators in conditional statements.
3. Memory overflow when storing more variables than allowed.

## 🧩 Limitations

1. This script is a basic parser and does not handle more advanced Python features like functions or classes.
2. Code formatting (e.g., spaces for indentation) is assumed to follow certain styles.

## 📈 Future Improvements

Potential enhancements include:

Support for while loops and more complex expressions.
1. Nested loops and conditionals.
2. Expanding the parser to handle functions and method calls.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
```
This `README.md` file includes all the essential sections to explain how the project works and how to use it. You can modify details like the file and script names as needed.
```
