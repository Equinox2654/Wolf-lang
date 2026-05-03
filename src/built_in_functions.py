import re

def wolf_print(line: str, variables: dict) -> None:
    match = re.match(r'^print\((.*)\)', line)
    if match:
        string = match.group(1)
        if re.search(r'(.*)', string):
            print(string.strip('"'))
        elif string in variables:
            print(variables[string])
        else:
                raise Exception("Variable does not exist or invalid string")

