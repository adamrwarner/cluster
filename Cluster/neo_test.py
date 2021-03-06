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
                                time_node = row[0]#a/n                                
                                OS_node = row[2]#b/m
                                IS_node=row[3]#c/o
                                port_node=row[4]#d/p
                                DS_node=row[5]#e/q
                                IC_node=row[6]#f/r                               
                                date_prop=row[1]#h                                
                                
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
                                                                
                                RE_node=row[7]
                                renodes=RE_node.split("|")
                                for x in renodes:
                                    if not x.strip():
                                        pass
                                    else:
                                        hkey=x#i/s
                                        #continue
                                        query2 = neo4j.CypherQuery(graph_db,
                                        """CYPHER 2.0
                                            merge (n:Incident {Time: {h}, Date:{a}, STIX:'Incident', id:'Incident'})
                                            merge (s:Indicator {Registry_Entries_Modified_or_Created: {g}, STIX:'Indicator', id:'Indicator'})                                                                                                                                   
                                            merge (n)-[r:Incident_Indicator]->(s)
                                            """)
                                        result2=query2.execute(a=time_node, g=hkey, h=date_prop)
                                                                                                                        
                                result = query.execute(a=time_node, b=OS_node, c=IS_node, d=port_node, e=DS_node, f=IC_node, h=date_prop)                              
                        except Exception as e:
                            print e
                            continue
if __name__ == '__main__':
    main()