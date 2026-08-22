from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the animals collection in the aac MongoDB database."""

    def __init__(self, username, password):
        # Connection variables for the Codio-hosted MongoDB instance
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize the authenticated connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' %
                                  (username, password, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """Insert one document. Returns True on success, False otherwise."""
        try:
            if data is not None:
                result = self.collection.insert_one(data)
                return result.acknowledged
            else:
                raise Exception("Nothing to save, because data parameter is empty")
        except Exception as e:
            print("An error occurred during create: %s" % e)
            return False

    def read(self, query):
        """Query documents. Returns a list of matching documents."""
        try:
            if query is not None:
                return list(self.collection.find(query))
            else:
                raise Exception("Nothing to find, because query parameter is empty")
        except Exception as e:
            print("An error occurred during read: %s" % e)
            return []

    def update(self, query, new_values):
        """Update all matching documents. Returns the number modified."""
        try:
            if query is not None and new_values is not None:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            else:
                raise Exception("Nothing to update, because a parameter is empty")
        except Exception as e:
            print("An error occurred during update: %s" % e)
            return 0

    def delete(self, query):
        """Delete all matching documents. Returns the number removed."""
        try:
            if query is not None:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                raise Exception("Nothing to delete, because query parameter is empty")
        except Exception as e:
            print("An error occurred during delete: %s" % e)
            return 0
