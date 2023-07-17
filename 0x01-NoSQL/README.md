#Learning No SQL databses

Tasks
0. List all databases
Write a script that lists all databases in MongoDB.

1. Create a adatabase
Write a script that creates or uses the database my_db

2. Insert document
Write a script that inserts a document in the collection school:

The document must have one attribute name with value “Holberton school”
The database name will be passed as option of mongo command

3. All documentss
Write a script that lists all documents in the collection school:

The database name will be passed as option of mongo command

4. All matches
Write a script that lists all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command

5. Count
Write a script that displays the number of documents in the collection school:

The database name will be passed as option of mongo command

6. Update
Write a script that adds a new attribute to a document in the collection school:

The script should update only document with name="Holberton school" (all of them)
The update should add the attribute address with the value “972 Mission street”
The database name will be passed as option of mongo command

7. Delete by match
Write a script that deletes all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command

8. List all documents in python Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object

9. Insert a document in python
Write a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id

10. Change School topics
Write a Python function that changes all topics of a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school

11. Where can I learn python 
Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched

12. Log status 
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
