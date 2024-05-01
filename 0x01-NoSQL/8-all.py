#!/usr/bin/env python3
"""
module containing a python function
that lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """ function that lists all documents in
        a collection
    """

    collection_list = [doc for doc in mongo_collection.find()]
    return collection_list
