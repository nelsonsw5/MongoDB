from pymongo import MongoClient
import csv
from tqdm import tqdm
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://nelsonsw5:joshuahiggins@assignmentdb.zh8eh.mongodb.net/AssignmentDB?retryWrites=true&w=majority")
db=client.business
#Step 2: Create sample data
file = open('/Users/stephennelson/Projects/MongoDB/tiktok.csv')
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()
for i in tqdm(range(len(rows))):
    user = { str(header[0]) : rows[i][0],
             str(header[1]) : rows[i][1],
             str(header[2]) : int(rows[i][2]),
             str(header[3]) : int(rows[i][3]),
             str(header[4]) : int(rows[i][4]),
             str(header[5]) : int(rows[i][5]),
             str(header[6]) : int(rows[i][6])
    }
    result = db.accounts.insert_one(user)
print("data has been updated")

