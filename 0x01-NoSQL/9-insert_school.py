#!/usr/bin/env python3
"""
inserting a new document in a collection based on kwargs
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """inser new doc into collection"""
    new_document_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_document_id
