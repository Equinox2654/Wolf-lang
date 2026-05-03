import re
from sys import argv
from os.path import isfile

variables = {}

def main():
    if len(argv) < 2 or not isfile(argv[1]):
        print(argv[1])
        print(isfile(argv[1]))
        raise Exception("Invalid file path provided")
    with open(argv[1]) as f:
        lines = f.readlines()
        f.close()
    new_lines = []
    for line in lines:
        new_lines.append(line.strip().strip("\n"))
    for line in new_lines:
        if re.search(r'^var ', line):
            match = re.match(r'^var (\w+)\s*=\s*(.*)', line)
            if match:
                var = match.group(1)
                value = match.group(2).strip('"')
                variables[var] = value
        if re.search(r'^print\((.*)\)', line):
            match = re.match(r'^print\((.*)\)', line)
            if match:
                string = match.group(1)
                if re.search(r'(.*)', string):
                    print(string.strip('"'))
                elif string in variables:
                    print(variables[string])
                else:
                    raise Exception(f"Variable does not exist or invalid string {new_lines.index(line)}")

if __name__ == "__main__":
    main()
