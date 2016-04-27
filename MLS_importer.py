#!/usr/bin/env python3

__author__ = 'ryshackleton'

import sys
import re
from pprint import pprint


def read_raw_lines(filename,outputfilename):
    parser = re.compile(r"(\d+)\s+(\d+)\s(\d+\s.+)=?\s(\d+)\s(\d{5,6})\s(\d{5,6})\s(\d)\s(\d+?\.?\d*)\s(\d+?\.?\d*)\s(\d+?\,?\d*)\s(\d{2})\/(\d{2})\/(\d{4})\s?(.*)")
    with open(outputfilename, mode='w', encoding='utf-8') as of:
        with open(filename, mode='rt', encoding='utf-8') as f:
            for line in f:
                matches = parser.match(line)
                commasep = ""
                if matches:
                    for word in matches.groups():
                        commasep += word + ","
                    of.write(commasep + "\n")
                else:
                    for word in line.strip().split():
                        commasep += word + ","
                    of.write(commasep + "\n")


def main(inputFileName,outputfilename):
    read_raw_lines(inputFileName,outputfilename)

if __name__ == '__main__':
    try:
        main(sys.argv[1],sys.argv[2])
    except IndexError as e:
        print("Incorrect command line arguments.")
        print("usage: MLS_importer.py InputFileName OutputFileName")





