#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on Dec 01, 2013
@author: AWARNER
'''

import csv
import sys
import os
from py2neo import neo4j,node, rel, cypher

def main():
    
    if len(sys.argv) < 2:
        sys.exit("Usage: neo_import.py input file path")
    else:        
        for root, dirs, files in os.walk(sys.argv[1]):            
            for f in files:                        
                if f.lower().endswith((".csv")):                    
                    f = os.path.join(root, f)            
                    graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")                        
                    with open(f, 'r+') as in_file:
                        #pathDict=[]
                        reader = csv.reader(in_file, delimiter = ',')
                        next(reader, None)        
                        batch = neo4j.WriteBatch(graph_db)                           
                        try:
                            for row in reader:    
                                time_node = row[0]#parameter {a} maps to node(n) and gets value from cell number 0 in each row in the csv                               
                                OS_node = row[2]#parameter {b} maps to node (m) and gets value from cell number 2 in each row in the csv
                                IS_node=row[3]#parameter {c} maps to node (o) and gets value from cell number 3 in each row in the csv
                                port_node=row[4]#parameter {d} maps to node (p) and gets value from cell number 4 in each row in the csv
                                DS_node=row[5]#parameter {e} maps to node (q) and gets value from cell number 5 in each row in the csv
                                IC_node=row[6]#parameter {f} maps to node (r) and gets value from cell number 6 in each row in the csv                               
                                date_prop=row[1]#parameter {h} is a property of node (n) and maps to cell number 1 in each row containing value in the csv                                                             
                                query = neo4j.CypherQuery(graph_db,
                                """CYPHER 2.0 
                                    merge (n:Incident {Time: {h}, Date:{a}, STIX:'Incident', id:'Incident'})
                                    merge (m:Indicator {Affected_Asset: {b}, STIX:'Indicator', id:'Indicator'})
                                    merge (o:Indicator {Infection_Source: {c}, STIX:'Indicator', id:'Indicator'}) 
                                    merge (p:Indicator {Infection_Port: {d}, STIX:'Indicator', id:'Indicator'})
                                    merge (q:Indicator {Detection_Signatures: {e}, STIX:'Indicator', id:'Indicator'})
                                    merge (r:Indicator {Infection_Chatter: {f}, STIX:'Indicator', id:'Indicator'})                                                        
                                    merge (n)-[:Affected_Asset]->(m)
                                    merge (n)-[:Infection_Source]->(o)
                                    merge (n)-[:Incident_Indicator]->(p)
                                    merge (n)-[:Incident_Indicator]->(q)
                                    merge (n)-[:Incident_Indicator]->(r)
                                    merge (n)-[:Incident_Indicator]->(s)                                    
                                    """)
                                    #each line creates a node or relationship by individual row in the csv.                            
                                    #several of the node properties are hard coded (they aren't updated by loop)
                                    #if we use the first node creating statement as an example:
                                    #merge (n:Incident {Time: {h}, Date:{a}, STIX:'Incident', id:'Incident'})
                                    #merge checks to see if the node has already been created
                                    #the node label can be edited e.g. "n:Incident", could change to "n:Cluster" etc
                                    #The property 'Time' is hard coded and can be changed. Its value is the parameter {h} which maps to cell number 0 in the csv
                                    #The property 'Date' is hard coded and can be changed, Its value is the parameter {a} which maps to cell number 1 in the csv
                                RE_node=row[7]
                                renodes=RE_node.split("|")
                                for x in renodes:
                                    if not x.strip():
                                        pass
                                    else:
                                        hkey=x#i/s
                                        query2 = neo4j.CypherQuery(graph_db,
                                        """CYPHER 2.0
                                            merge (n:Incident {Time: {h}, Date:{a}, STIX:'Incident', id:'Incident'})
                                            merge (s:Indicator {Registry_Entries_Modified_or_Created: {g}, STIX:'Indicator', id:'Indicator'})                                                                                                                                   
                                            merge (n)-[r:Incident_Indicator]->(s)
                                            """)
                                        result2=query2.execute(a=time_node, g=hkey, h=date_prop)#submits the cypher query to load nodes into the database                                                                                                                        
                                result = query.execute(a=time_node, b=OS_node, c=IS_node, d=port_node, e=DS_node, f=IC_node, h=date_prop)                              
                        except Exception as e:
                            print e
                            continue
if __name__ == '__main__':
    main()