#!/usr/bin/env python3
""" module that contains a function that returns 
    the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools having a specific topic """

    filtered_topics = {
      "topics": {
        "$elemMatch": {
           "$eq": topic,
         }, 
      }, 
    }
    list_of_topics = [topic for topic in mongo_collection.find(filtered_topics)]
