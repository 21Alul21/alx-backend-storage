#!/usr/bin/env python3
"""python module that contains a function
that changes all the topics of a school
"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics of a school document
    based on the name
    """

    mongo_colection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
