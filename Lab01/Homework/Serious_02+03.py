# mongodb://admin:admin@ds021182.mlab.com:21182/c4e
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# Connect to the database:
client = MongoClient(mongo_uri)
# Get the databse
db = client.get_default_database()
# Connect/create the collections
posts = db["posts"]

# # Read the collections "posts"
# read = post.find()
# first_row = read[1]
# print(first_row)

# Create a document

haids = {
    "title": "Lặng - JSOL",
    "author": "DSH",
    "content":
"""
    Nếu biết trước rằng sẽ mãi xa nhau 
    Nếu biết trước rằng sẽ mang thương đau ngày sau 
    Sao không níu lấy đôi tay ... thật lâu... 
    Để lời yêu thương nhạt màu 
    Nếu biết trước đường đời rẽ ngang đôi ta 
    Nếu biết trước lời hẹn ước sẽ trôi xa đi mất 
    Mây chợt hững hờ, đêm chợt bơ vơ 
    Hoài niệm giấu hết trong mưa 

    [Chorus] 
    Mùa thu đi qua 
    Trầm hương gọi bóng dáng người khuất xa 
    Đã lặng tiếng dương cầm 
    Gió mang mùa đông ghé lại 
    Để cô đơn xé nát tim ai 
    Giờ ta như mang 
    Trọn sầu nhân gian 
    Người nơi sương khói ân tình nay dở dang 
    Giấc mơ hóa tro tàn 
    Chẳng thể lướt thêm một phím đàn 
    Để hồn ta mãi còn lang thang 

    [Verse 2] 
    Lá đã úa màu tiễn bước cơn mơ 
    Bóng tối lấp mờ bức vẽ đơn sơ ngày xưa 
    Sao ta vẫn đứng nơi đây ngóng chờ 
    Lời hẹn ước như chưa bao giờ vụn vỡ 
    biết cát bụi hóa kiếp chơi vơi 
    Dẫu biết tiếng lòng sẽ xuôi về ngàn suối lặng trôi 
    Cớ sao bước vội, chẳng cất nên lời 
    Một lần sau cuối trước khi xa rời.
"""
}

# Update the document into the collections:
posts.insert_one(haids)
# Lúc insert tác giả viết nhầm trường author


