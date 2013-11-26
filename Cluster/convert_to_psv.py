#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv
import os
import sys


'''for filename in os.listdir(INPUT_DIR):
   with open(os.path.join(INPUT_DIR,filename), dialect='excel-tab') as infile:
      reader = csv.reader(infile)
      for row in reader:
          print row'''
    

def main():
    #enter your directory or file path here, separated by two \\ instead of singular \. ex: 'C:\\downloads\\projects\\blogpages\\'
    fname = raw_input("Enter filepath with files to be converted:")
    #print "File location = %s" % fname
    #enter desired name for file output in.csv
    
    #enter desired column heads for fields being parsed in html
    #writer.writeLine(["url", "headline", "name"])
        
    #Main Function
    for root, dirs, files in os.walk(fname):
        for f in files:
            #url = os.path.join(root, f)
            #url = os.path.dirname(url).split(topdir)[1]
            #url = url.split('\\')[0]
            #depending on the file level of the individual html being parsed you may 
            #need to include the following split to get to the url in the file path
            #url = url.split('\\')[0]
            
            if f.lower().endswith((".tsv")):
                print "working.."
                f.open(os.path.join(root, f), "w").write(fname +".csv")
                #print "more work"
                #blog = {}                               
                #for row in csv.reader(sys.stdin):
                #print "work work"
                #print "\t".join(row)
                #f.write(file_new +".csv")
                f.close()                    
                #output sequence - writes the values from each of the stored labels to the .csv
                #seq = [url, unicode(blog.get('title')), unicode(blog.get("name")), unicode(blog.get("persianDate"))]
                #writer.writeLine(seq)
    #return ""
if __name__ == '__main__':
    main()
    print "Finished"

