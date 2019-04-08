import pymongo

pymongo.MongoClient()['school']['stu'].insert_one({'name': 'liu', 'age': 20})