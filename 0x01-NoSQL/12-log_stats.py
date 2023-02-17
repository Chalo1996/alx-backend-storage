#!/usr/bin/env python3
""" 12-log_stats module."""


#import the mongo client
from pymongo import MongoClient


#connect to the mongo client
client = MongoClient('mongodb://127.0.0.1:27017')


#select the database collection name
logs = client.logs.nginx

#find the number of documents in the collection
print(f'{logs.count_documents({})} logs')
print('Methods:')
print(f'\tmethod GET: {logs.count_documents({"method": "GET"})}')
print(f'\tmethod POST: {logs.count_documents({"method": "POST"})}')
print(f'\tmethod PUT: {logs.count_documents({"method": "PUT"})}')
print(f'\tmethod PATCH: {logs.count_documents({"method": "PATCH"})}')
print(f'\tmethod DELETE: {logs.count_documents({"method": "DELETE"})}')
print(f'{logs.count_documents({"path": "/status"})} status check')
