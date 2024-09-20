import os

max_vars = 10
tab_spaces = 8
current_directory = __file__
file_name = "pycode.txt"
file_path = os.path.join(current_directory + "/../", file_name)


with open(file_path, "r") as f:
    lines = f.readlines()

keywords = set()
internal_functions = set()
operators = set()
variables = {}
numbers = {}
symbols = {}
words = {}
output = ""
line_number = 0
in_indent = False


def doMath(a, b, c):
    if variables.get(a, None) is not None:
        val1 = float(variables[a])
    elif a.isdigit():
        val1 = int(a)
    elif "." in a:
        val1 = float(a)
    else:
        print(f"Err1: variable is {a} not defined")

    if variables.get(c, None) is not None:
        val2 = float(variables[c])
    elif c.isdigit():
        val2 = int(c)
    elif "." in c:
        val2 = float(c)
    else:
        print(f"Err2: variable is {c} not defined")

    if b == "+":
        return val1 + val2
    elif b == "-":
        return val1 - val2
    elif b == "*":
        return val1 * val2
    elif b == "/":
        return val1 / val2
    else:
        print("Unknown Operation")
        exit(1)


for line in lines:
    in_qoute = False
    line_number += 1

    if not line:
        continue

    if " " * tab_spaces not in line:
        in_indent = False

    if in_indent is False:
        words = []

    h = ""
    isEqual = False
    newLine = ""

    if "==" in line:
        idx = -1
        k = 0
        for ch in line:
            if isEqual and ch == "=":
                newLine += "$"
                isEqual = False
            elif ch == "=":
                isEqual = True
            else:
                newLine += ch
            k = k + 1
        line = newLine

    isEqual = False
    newLine = ""
    if "!=" in line:
        idx = -1
        k = 0
        for ch in line:
            if isEqual and ch == "=":
                newLine += "@"
                isEqual = False
            elif ch == "!":
                isEqual = True
            else:
                newLine += ch
            k = k + 1
        line = newLine

    for ch in line:
        if ch == "\n":
            break

        if ch in ["'", '"']:
            if in_qoute is False:
                in_qoute = True
            else:
                in_qoute = False
        if in_qoute is True or ch not in [
            " ",
            "(",
            ")",
            ":",
            ",",
            "+",
            "*",
            "-",
            "/",
            "^",
            "%",
            "=",
        ]:
            h += ch
        elif ch in [":", "+", "*", "-", "/", "^", "%", "="]:
            if h != "":
                words.append(h)
            h = ""
            words.append(ch)
        elif in_qoute is False:
            if h != "":
                words.append(h)
            h = ""
        else:
            words.append(ch)

    if h != "":
        words.append(h)
    if len(words) == 0:
        continue
    if in_indent is True and words[-1] != "\n":
        words.append("\n")
    #

    if in_indent is False and words[-1] == ":":
        in_indent = True
        continue

    if words[0] == "if":
        doElse = False
        keywords.add(words[0])
        condition = words[1]
        operator = ""
        variable_name1 = ""
        variable_name2 = ""
        for ch in condition:
            if ch in ["=", "<", ">", "!", "$", "@"]:
                operator += ch
            else:
                if operator == "":
                    variable_name1 += ch
                else:
                    variable_name2 += ch
        operators.add(operator)
        if variable_name1 not in variables:
            print(f"Error: Variable1 '{variable_name1}' is not defined.")
            exit(1)
        if variable_name2 not in variables:
            print(f"Error: Variable2 '{variable_name2}' is not defined.")
            exit(1)

        if operator == "$":
            condition = int(variables[variable_name1]) == int(variables[variable_name2])
        elif operator == "@":
            condition = int(variables[variable_name1]) != int(variables[variable_name2])
        else:
            print(f"Error: Invalid comparison operator '{operator}'.")
            exit(1)

        if condition and words[3] == "print":
            output += words[4][1:-1] + "\n"
            internal_functions.add(words[3])
        else:
            doElse = True
    elif words[0] == "else":
        keywords.add(words[0])
        if doElse is True and words[2] == "print":
            output += words[3][1:-1] + "\n"
            internal_functions.add(words[2])
    elif words[0] == "for":
        keywords.add(words[0])
        if words[2] == "in" and words[3] == "range":
            keywords.add(words[2])
            internal_functions.add(words[3])

            if len(variables) < max_vars:
                variable_name = words[1]
                variable_value = words[4]
                variables[variable_name] = variable_value
                print(f"variable {variable_name} has been created")
            else:
                print("memory is full for new variable")
                exit(1)

            if len(words) < 8:
                continue
            if words[5] == ":":
                if words[6] == "print":
                    output += (words[7][1:-1] + "\n") * (int(words[4]))
                else:
                    for t in range(int(int(words[4]))):
                        if words[7] == "=":
                            if len(words) == 12:
                                variables[words[6]] = doMath(
                                    words[8], words[9], words[10]
                                )
                            elif len(words) == 10:
                                if variables.get(words[8], False):
                                    variables[words[6]] = variables[words[8]]
                                else:
                                    print(f"Error4: Variable {words[8]} is not defined")
                            else:
                                print("not implemented2")
                                exit(1)
                    while words[-1] != ":":
                        words.pop()
            elif words[6] == ":":
                if words[4].isdigit():
                    t1 = int(words[4])
                else:
                    if variables.get(words[4], False):
                        t1 = int(variables[words[4]])
                    else:
                        print("Error: variable '" + words[4] + "' is not defined2")
                if words[5].isdigit():
                    t2 = int(words[5])
                else:
                    if variables.get(words[5], False):
                        t2 = int(variables[words[5]])
                    else:
                        print("Error: variable '" + words[5] + "' is not defined2")

                for t in range(t1, t2):
                    variables[variable_name] = t

                    if words[7] == "print":
                        if words[8].isdigit():
                            val = int(words[8])
                        else:
                            if variables.get(words[8], False):
                                val = int(variables[words[8]])
                            else:
                                val = words[8]
                        output += str(val) + "\n"
                    else:
                        if words[8] == "=":
                            if len(words) == 13:
                                variables[words[7]] = doMath(
                                    words[9], words[10], words[11]
                                )
                            elif len(words) == 11:
                                if variables.get(words[9], False):
                                    variables[words[7]] = variables[words[9]]
                                else:
                                    print(f"Error5: Variable {words[9]} is not defined")
                            else:
                                print("not implemented3")
                                exit(1)
                while words[-1] != ":":
                    words.pop()
            else:
                print("ERROR FOR")
                exit(1)
    elif words[0] == "print":
        keywords.add(words[0])
        internal_functions.add(words[0])
        for i in range(1, len(words)):
            variable_name = words[i]
            if variables.get(variable_name, False):
                output += str(variables[variable_name]) + " "
            elif variable_name[0] == "'" and variable_name[-1] == "'":
                output += variable_name[1:-1] + " "
            elif variable_name[0] == '"' and variable_name[-1] == '"':
                output += variable_name[1:-1] + " "
            else:
                print("ERROR2 Variable '" + variable_name + "' is not defined")
                exit(1)
        output += "\n"
    else:
        if len(variables) < max_vars:
            if words[1] == "=":
                operators.add(words[1])
                variable_name = words[0]
                variable_value = words[2]
                variables[variable_name] = variable_value
            else:
                output += str(doMath(words[0], words[1], words[2])) + "\n"
        else:
            print("Error: memory is full.")


print("keywords:", ",".join(keywords))
print("internal function:", ",".join(internal_functions))
print("operators:", ",".join(operators))
for var in variables:
    print(var, "=", variables[var])

outputs = []
h = ""
for o in output:
    for ch in o:
        if ch == ",":
            if h != "":
                outputs.append(h)
                h = ""
        else:
            h += ch
if h != "":
    outputs.append(h)

print("\n".join(outputs))
