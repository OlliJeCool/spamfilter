import os


def read_classification_from_file(filename: str):
    '''Helper function for reading classifications from a file, returns them in a dictionary.'''
    output = {}
    with open(f'{filename}', "rt", encoding="utf-8") as f:
        for line in f.readlines():
            values = line.split(" ")
            output[values[0]] = values[1].strip()
    return output

def write_classification_to_file(filepath:str, classification: dict):
    '''Helper function for writing classifications from a dictionary to a file.'''
    with open(f'{filepath}', "wt", encoding="utf-8") as f:
        for name, tag in classification.items():
            f.write(f'{name} {tag}\n')


def path_exists(filepath: str):
    '''Verifies if a directory exists.'''
    return os.path.isdir(filepath)