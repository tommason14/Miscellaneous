#!/usr/bin/env python3

import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--columns', help='Number of columns to extract', required=True, type=int)
parser.add_argument('-r', '--rows', help='Number of rows to extract', type=int)
parser.add_argument('-p', '--pdf', help='Pdf file containing the data', required=True)
parser.add_argument('-o', '--output', help='Filename of csv that is produced', required=True)
parser.add_argument('--keep-first', action='store_true',
help='Keep the first table if two are printed on the same line')
parser.add_argument('--keep-second', action='store_true',
help='Keep the second table if two are printed on the same line')
parser.add_argument('args', nargs=argparse.REMAINDER)
cli = parser.parse_args()

def pdf_data(file):
    """
    Return pdf as a list of strings
    """
    return subprocess.run(f'pdftotext {file} -layout -', 
        shell=True, stdout=subprocess.PIPE, 
        encoding='utf-8').stdout.split('\n')

def check_number_of_args(args):
    """
    Quits if an odd number of arguments are supplied
    """
    if not len(args) % 2 == 0:
        sys.exit('Must supply an even number of arguments')

def group_args_into_pairs(lst):    
    """
    Takes in sys.argv[1:] and returns tuples of 
    consecutive pairs
    """
    pairs=[]
    for ind1, i in enumerate(lst):
        for ind2, j in enumerate(lst):
            firsts = [val[0] for val in pairs]
            seconds = [val[1] for val in pairs]
            if (
            ((ind1 + 1) % 2 != 0) and 
            ((ind2 + 1) % 2 == 0) and 
            i not in firsts and 
            j not in seconds):
                pairs.append((i, j))
    return pairs
 
def extract_data(pdf, item1, item2):
    """
    Searches for data between `item1` and `item2` in the 
    list `pdf`.
    Note this includes the lines with `item1` and `item2` in.
    """
    ret = []
    first_found = False
    second_found = False
    for line in pdf:
        if item1 in line:
            first_found = True
        if first_found and not second_found:
            print(line.split())
            ret.append(line)
        # place here to only register after line has been printed
        if first_found and item2 in line:
            second_found = True
    return ret

def format_line(lst):
    """
    Turns the list into a comma-separated string with a
    newline character added
    """
    return ','.join(lst) + '\n'

def extract_tables(pairs, pdf):
    """
    Loops over the pairs and extracts data
    """
    data = []
    for pair in pairs:
        data.append(pair[0] + '\n')
        extracted = extract_data(pdf, *pair)
        # len_extracted = len(extracted)
        for line in extracted:
            split_line = line.split()
            if len(split_line) == cli.columns and not cli.keep_second:
                data.append(format_line(split_line))
            # deal with cases when two tables are printed side-by-side
            if len(split_line) == 2 * cli.columns:    
                multiples = tables_side_by_side(split_line)
                first_table, second_table = multiples
                data = append_multiple_tables(first_table,        
                second_table, data) 
            # data in wrong order if first table ends before second
            if len(split_line) == cli.columns and cli.keep_second:
                data.append(format_line(split_line))
    return data

def append_multiple_tables(first_table, second_table, data):
    """
    Appends the table depending on whether the user has included
    `keep_first` or `keep_second` in the program call
    """
    if cli.keep_first:
        data.append(first_table) 
    if cli.keep_second:
        data.append(second_table)
    return data

def all_floats(lst):
    """
    Tests if all items of the list can be cast to a float
    """
    results = []
    numeric = False
    for value in lst:
        try:
            value = float(value)
            numeric = True
        except ValueError:
            pass
        results.append(numeric)
    if all(item for item in results):
        return True
    return False

def tables_side_by_side(split_line):
    """
    Deal with cases when two tables are printed on the same line
    """
    if len(split_line) == cli.columns * 2: 
        if all_floats(split_line):        
            first_table = format_line(split_line[:cli.columns])
            second_table = format_line(split_line[cli.columns:])
            return first_table, second_table
        else:
            print(split_line)
            if cli.keep_first:
                first_table = format_line(split_line[:cli.columns])
                return first_table, None
            if cli.keep_second:
                second_table = format_line(split_line[cli.columns:])
                print(second_table)
                return None, second_table
    if len(split_line) == cli.columns and cli.keep_first:
        return format_line(split_line), None
    if len(split_line) == cli.columns and cli.keep_second:
        return None, format_line(split_line)

def write_to_file(filename, data):
    if len(data) > 1: #first pair name
        with open(filename, 'w') as f:
            for line in data:
                f.write(line)

def main():
    check_number_of_args(cli.args)
    pairs = group_args_into_pairs(cli.args)
    pdf = pdf_data(cli.pdf)
    data = extract_tables(pairs, pdf)
    write_to_file(cli.output, data)

if __name__ == '__main__':
    main()
