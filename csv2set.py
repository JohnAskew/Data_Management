import csv
import os
import sys
''' name: csv2set.py
    desc: Read csv, clean header and return list of sets
    usage: python header2tuple STOCK-ABBRV (ex. EBAY)
    '''

def check_for_filename(filename):
    if os.path.exists(filename):
        return True
    else:
        return False
    
def read_header2list(filename):
    if check_for_filename(filename):
        records = []
        with open(filename) as filename:
            rows = csv.reader(filename)
            header = next(rows)
            for row in rows:
                row = set(row)
                records.append(row)
            print("Set sample being returned:",records[0])
            return records
    else:
        print("File: " + filename + " not found. Skipping list create")
                
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = sys.argv[1]
        else:
            filename = 'AMZN.csv'
    else:
        filename = 'AMZN.csv'
        
read_header2list(filename)