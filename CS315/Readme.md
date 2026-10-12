# Database Systems Comparison Project

## Overview
This project compares three different database paradigms:
- Relational (PostgreSQL)
- Document-based (MongoDB)
- Graph-based (Neo4j)

All systems are evaluated on a common dataset using similar queries such as joins, aggregations, and relationship traversal.

---

## Files Description

### 1. xml_to_csv.py
This script converts the original XML dataset into CSV format.  
It parses large XML files efficiently and extracts all attributes into structured CSV files for further processing.

---

### 2. mongo_flat_to_nested.py
This script transforms flat relational-style data into a nested MongoDB format.  
It groups:
- Comments under Posts  
- Posts under Users  
- Badges under Users  

Finally, it inserts the nested documents into MongoDB for efficient document-based querying.

---

### 3. MongoDB.txt
Contains queries executed on the **flat MongoDB schema**, similar to relational structure.  
Includes operations like filtering, aggregations, joins (via lookup), and performance benchmarking.

---

### 4. MongoDB_nested.txt
Contains queries on the **deeply nested MongoDB schema**, where posts and comments are embedded within users.  
Demonstrates how nesting affects query complexity and performance.

---

### 5. Neo4j.txt
Contains Cypher queries used for the graph database (Neo4j).  
Focuses on relationship traversal, pattern matching, and graph-based querying. 

---

### 6. PostGreSQL.txt
Contains SQL queries executed on PostgreSQL.  
Includes joins, aggregations, and complex queries for comparison with NoSQL and graph databases. 

---

### 7. evaluation.py
This file is intended for running performance evaluations and benchmarking queries across different databases.





