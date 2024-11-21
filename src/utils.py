import re

def read_classification_from_file(filename: str):
    output = {}
    with open(f'{filename}', "rt", encoding="utf-8") as f:
        for line in f.readlines():
            values = line.split(" ")
            output[values[0]] = values[1].strip()
    return output

def write_classifictaion_to_file(filepath:str, classification: dict):
    with open(f'{filepath}', "wt", encoding="utf-8") as f:
        for line in classification.items():
            match = re.search(r"'([^']*)'", str(line[0]))
            if match:
                name = match.group(1)
            f.write(f'{name} {line[1]}\n')