#!/usr/bin/env python3
"""
function returnng the list of school having a specific topic
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """Find all schools that have the given topic"""
    schools_with_topic = mongo_collection.find({"topics": topic})

    """Convert the cursor to a list of ditioaries"""
    result = list(schools_with_topic)

    return result
