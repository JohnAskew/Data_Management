import csv
import os
import sys
''' name: header2tuple.py
    desc: Read csv, clean header and return list of tuples
    usage: python header2tuple STOCK-ABBRV (ex. EBAY)
    '''

def check_for_filename(filename):
    if os.path.exists(filename):
        return True
    else:
        return False
    
def read_header2tuple(filename):
    if check_for_filename(filename):
        myheaderlist = []
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            header = next(rows)
            col_cnt = len(header)
            for col in range(len(header)):
                col = str(header[col]).replace( ' ', '_').replace('.','_')
                myheaderlist.append(col)
            for row in rows:
                for key, value in enumerate(row):
                    myheaderlist[key] = row[key]
                    row = tuple(row)
                records.append((row))
            print("Tuple sample of what is being returned:",records[0])
            return records
    else:
        print("File: " + filename + " not found. Skipping tuple create")
                
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = sys.argv[1]
        else:
            filename = 'AMZN.csv'
    else:
        filename = 'AMZN.csv'
        
read_header2tuple(filename)