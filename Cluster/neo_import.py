#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on Dec 01, 2013
@author: AWARNER
'''

import csv
from py2neo import neo4j, node, rel
import sys

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")


if len(sys.argv) < 2:
    sys.exit("Usage: neo_import.py input_filename")
else:
    
    with open((sys.argv[1]), 'rb') as in_file:
    
        reader = csv.reader(in_file, delimiter = '|')
        headers = next(reader, None)
        
        batch = neo4j.WriteBatch(graph_db)
        
        for h in headers:
            rel1 = (headers[0]) 
            node1 = (headers[1])
            node2 = (headers[2])
            
        for row in reader:
            
            for col in row:
                src_ip = row[1]
                dst_ip = row[2]
                instance = row[0]
                packets = row[6]
                length = row[7]
                src_port=row[10]
                dst_port=row[11]
                protocol=row[13]
                #src_ip_node=batch.get_or_create_indexed_node('IPs', node1, src_ip, {'src_port':src_port})
                #dst_ip_node=batch.get_or_create_indexed_node('IPs', node2, dst_ip, {'dst_port':dst_port})
                #batch.get_or_create_indexed_relationship(index="Attacks", key=rel1, value=instance, start_node=src_ip_node, type_='type', end_node=dst_ip_node, properties={"instance":instance, "protocol":protocol, "packets":packets, "Length":length})
                src_ip_node = batch.create(node(src_ip=src_ip, src_port=src_port))
                dst_ip_node = batch.create(node(dst_ip=dst_ip, dst_port=dst_port))
                
                batch.create(rel(src_ip_node, ("Attacks", {"instance":instance, "protocol":protocol, "packets":packets, "length":length}), dst_ip_node))
                print "stuff is happening"
        batch.submit() 
            
                