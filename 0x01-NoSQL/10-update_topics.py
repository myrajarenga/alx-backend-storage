#!/usr/bin/env python3
"""
changes to all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """updating school with given name"""
    result = mongo_collection.update_one\
            ({"name": name}, {"$set": {"topiss": topics}})

    return result.modified_count > 0
