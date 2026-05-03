import re

def check_and_store_vars(line: str, variables: dict) -> None:
    match = re.match(r'^var (\w+)\s*=\s*(.*)', line)
    if match:
        var = match.group(1)
        value = match.group(2).strip('"')
        variables[var] = value
