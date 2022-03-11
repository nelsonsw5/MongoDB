from pymongo import MongoClient
client = MongoClient("mongodb+srv://nelsonsw5:joshuahiggins@AssignmentDB.zh8eh.mongodb.net/AssignmentDB?retryWrites=true&w=majority")
db=client.business
cursor = db['accounts'].aggregate([
    {"$match" : {"Subscribers": { "$gte": 100000000 }}
    },
    { "$group": { "_id": "null", "Account": { "$sum": 1 }} }
    ]);
for document in cursor:
    print("number of accounts with more than 100,000,000 subscribers: ", document)
cursor = db['accounts'].aggregate([
    {"$match" : {"Subscribers": { "$gte": 100000000 }}
    }
    ]);
for document in cursor:
    print(document)
cursor = db['accounts'].aggregate([
   { "$match": { "$or": [ { "Subscribers": { "$gt": 10000000} }, { "Shares": { "$gte": 100000} } ] } },
  { "$group": { "_id": "Null", "Account": { "$sum": 1 } } }
] );
for document in cursor:
    print("number of accounts with more than 100,000,000 subscribers and average shares greater than 100,000: ", document)


