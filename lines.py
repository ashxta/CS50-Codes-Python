import sys

no_lines = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        for raw_line in file:
            line = raw_line.lstrip()

            if not (line.startswith("#") or line == ""):
                no_lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(no_lines)