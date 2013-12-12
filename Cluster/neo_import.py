#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on Dec 01, 2013
@author: AWARNER
'''

import csv
from pprint import pprint
from py2neo import neo4j, node, rel
import sys

in_file  = open("C:/Users/awarner/git/cluster/Cluster/exploit.csv", "rb")
reader = csv.reader(in_file)

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
batch = neo4j.WriteBatch(graph_db)
#print graph_db.get_reference_node()

'''if len(sys.argv) < 2:
    sys.exit("Usage: neo_import.py input_filename")
else:
    ifile  = open(sys.argv[1], "rb")
    reader = csv.reader(ifile)'''

for line in in_file.readlines():
    split_line = line.split('\t')
    user_id = split_line[0]
    user_followers = split_line[0]
    user_followers_list = user_followers.split("\t")
    
    batch.get_or_create_indexed_node("Users", "user_id", user_id,{"user_id":user_id})
    print "created user node"
    
    for user_follower in user_followers_list:
        batch.get_or_create_indexed_node("Users", "user_id", user_id, {"user_id":user_id})
        print "created follower node"
    nodes = batch.submit() 
