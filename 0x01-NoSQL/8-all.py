#!/usr/bin/env python3
""" Module 8-all """


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    docs = []

    if mongo_collection is None:
        return docs

    for c in mongo_collection.find({}):
        docs.append(c)

    return docs
