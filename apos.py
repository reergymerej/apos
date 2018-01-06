#!/usr/bin/env python3.6
import sys

try:
    file_name = sys.argv[1]
    with open(file_name, 'r') as input_file:
        input_value = input_file.read()
except:
    print("unable to read input file")
    sys.exit(1)

def make_replacements(input_value):
    return input_value.replace("'", "’")

output_value = make_replacements(input_value)

print(output_value)
