from pymongo import MongoClient
import config

cluster = MongoClient(config.uri)
db = cluster.mongodb_py