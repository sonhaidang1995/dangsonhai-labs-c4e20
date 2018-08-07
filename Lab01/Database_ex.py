# DATABASE
# pip install pymongo

from pymongo import MongoClient

mongo_uri = "mongodb://database1:database1@ds113402.mlab.com:13402/c4e20-labs"
# Host: ds113402.mlab.com
# Port: 13402
# database name: c4e20-labs
# <dbuser>:<dbpassword>: user and pass database

# 1. Connect to the database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# # 4. Create a document
# new_game = {
#     "title": "Hứng bia",
#     "description": "Hứng bia lột đồ"
# }

# # 5. Insert document into collection
# games.insert_one(new_game)

# # Muốn Read database cần phải comment 4, 5 lại

# 6. Read all documents
all_game = games.find()
first_game = all_game[1]
print(first_game["title"])