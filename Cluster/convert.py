#!/usr/bin/env python

import csv
import sys
import os

if len(sys.argv) < 4:
    sys.exit("Usage: convert.py ~/dir .tsv .csv")
else:    
    cur_dir, old_ext, new_ext = sys.argv[1:]
    for filename in os.listdir(cur_dir):
        filename = os.path.join(cur_dir, filename)
        base, file_ext = os.path.splitext(filename)
        if file_ext == old_ext:
            newfile = base + new_ext
            csv.field_size_limit(sys.maxsize)
            with open(filename, 'rb') as ifh, open(newfile, 'wb') as ofh:
                reader = csv.reader(ifh, delimiter='\t')
                #seq = ( (r[0], r[1], r[3], r[4]) for r in reader)
                #csv.writer(ofh, delimiter='|').writerows(seq)
                csv.writer(ofh, delimiter='|').writerows(reader)
            os.unlink(filename)