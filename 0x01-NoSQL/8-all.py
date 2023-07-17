#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""


import pymongo


def list_all(mongo_collection):
    """ Return lst of all documents in the the collection"""
    if mongo_collection is None:
        return []
    documents = mongo_collection.find()
    return [documents for documents in documents]
