from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect the database:
client = MongoClient(mongo_uri)
# Get the database
data = client.get_default_database()
# Update the collection
cus = data["customers"]
# Read the document
# read = cus.find()
# first = read[1]
# print(first)
num = cus.count()
num_ads = cus.find({"ref":"ads"}).count()
num_events = cus.find({"ref":"events"}).count()
num_wom = cus.find({"ref":"wom"}).count()

# import tính năng
import matplotlib
from matplotlib import pyplot
matplotlib.use('tkAgg')
# Tính giá trị các values
a = num_ads/num*100
b = num_events/num*100
c = 100 - a - b
# Chuẩn bị số liệu
labels = ["events","ads","wom"]
colors = ['red','blue','yellow']
values = [a,b,c]
explode = [0,0,0.1]
# Vẽ biểu đồ
pyplot.pie(values, labels= labels,colors = colors, explode = explode)
pyplot.axis('equal')
# Hiển thị biểu đồ
pyplot.show()