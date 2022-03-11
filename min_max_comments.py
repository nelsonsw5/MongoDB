from pymongo import MongoClient
from pymongo import ASCENDING
client = MongoClient("mongodb+srv://nelsonsw5:joshuahiggins@AssignmentDB.zh8eh.mongodb.net/AssignmentDB?retryWrites=true&w=majority")
db=client.business

cursor = db['accounts'].aggregate([
    {"$sort":{"Likes": ASCENDING}},
    {"$group" : 
    {"_id" :"$Null", "leastcomments" : {"$first" :"$Comments"},
                    "mostcomments"  : {"$last" :"$Comments"}
                    
    }}
    ]);
for document in cursor:
    print("min/max number of average comments: ", document)