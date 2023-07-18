#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""



import pymongo
from collections import Counter


def connect_to_mongodb():
    """connect to mongoDB instead of localhost"""
    client = pymongo.MongoClient('localhost',  27017)
    db = client['logs']
    collection = db['nginx']
    return collection

def get_log_count(collection):
    """count collection of documents"""
    return collection.count_documents({})

def get_method_counts(collection):
    """get method counts"""
    methods = ['GET', 'POST', 'PUT' 'PATCH', 'DELETE']
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})
        return method_counts
def get_status_endpoint_count(collection):
    """status of method"""
    return collection.count_documents({"method": "GET", "path": "/status"})


if __name__ == "__main__":
    collection = connect_to_mongodb()

    # Get the total log count
    total_logs = get_log_count(collection)

    # Get the method counts
    method_counts = get_method_counts(collection)

    # Get the count of logs with method=GET and path=/status
    status_endpoint_count = get_status_endpoint_count(collection)

    # Display the statistics
    print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")
    print("second line: Methods:")
    for method, count in method_counts.items():
        print(f"\t{count} logs with method={method}")

    print(f"{status_endpoint_count} logs with method=GET and path=/status")
