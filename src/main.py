import re
from sys import argv
from os.path import isfile
from variables import check_and_store_vars
from built_in_functions import wolf_print

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
            check_and_store_vars(line, variables)
        if re.search(r'^print\((.*)\)', line):
            wolf_print(line, variables)

if __name__ == "__main__":
    main()
