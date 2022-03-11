from pymongo import MongoClient
client = MongoClient("mongodb+srv://nelsonsw5:joshuahiggins@AssignmentDB.zh8eh.mongodb.net/AssignmentDB?retryWrites=true&w=majority")
db=client.business
cursor = db['accounts'].aggregate([
    {"$match" : {"Account" : "billieeilish"}}
    ])
for document in cursor:
    print(document)


