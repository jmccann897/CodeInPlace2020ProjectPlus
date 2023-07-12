# Testing CSV file manipulation

import csv
import os


with open('c:\\Users\\JJ\\Documents\\MyPythonScripts\\Espacenet Search\\test.csv')as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count < 6:
            line_count +=1
        elif line_count == 6:
            print(f'Column names are {", ".join(row)}')
            line_count +=1
        elif line_count > 6:
            print(f'\t{row[2]} created {row[1]} which was published on {row[8]}.')
            line_count +=1
    
