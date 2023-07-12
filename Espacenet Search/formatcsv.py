import csv

def find_header(reader):
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)

   
f = open ('c:\\Users\\JJ\\Documents\\MyPythonScripts\\Espacenet Search\\t1.csv', 'rt')
reader = csv.reader(f)

out= open('c:\\Users\\JJ\\Documents\\MyPythonScripts\\Espacenet Search\\first_edit.csv', 'w+', newline='')
writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
# create find_header function
find_header(reader)

for row in reader:
    writer.writerow(row)













