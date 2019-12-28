
import pymongo # 몽고 디비를 가져옴.
# 몽고디비 접속
DB_HOST = '127.0.0.1:27017'
DB_ID = 'rhrhrkfl'
DB_PW = 'rlawns%2425'

client = pymongo.MongoClient("mongodb+srv://rhrhrkfl:rlawns%2425@junseonfirst-o8wgi.gcp.mongodb.net/test?retryWrites=true&w=majority")
# db 객체 할당받기
db = client.test

# collection 객체 할당받기
collection = db['testcoll'] # 무슨 역할인지 모름
# collection = db.coll_이름 으로도 사용 가능.









# 도큐먼트 생성
import datetime
post = {
    'author': "junseon",
    "text": 'My first db',
    'tags': ["mongodb", 'python', 'pymongo'],
    'date': datetime.datetime.utcnow()
}
# 도큐먼트 insert 하기
coll = db.collection # db.collection 을 coll이라고 부르기로 함. collection은 컬렉션의 이름이다.
# coll은 client.test.collection.
coll.insert_one(post)
# post_id = coll.insert(post)

# 만든 document를 수정 혹은 추가하기
client.test.collection.update_one( # update_many는 조건에 맞는 모든 document를 수정한다.
    {"author": "tester"}, # 검색 조건이다. 이 조건에 맞는 것 하나만 업데이트 한다.
    {
        "$set": # 업데이트할 것을 말한다. 필수다.
            {"abcd":"try again"} # 업데이트할 내용이다.
    }
)
# 만든 document를 제거하기
client.test.collection.delete_one({"author":"tester"}) # 조건에 맞는 하나만 삭제

update_many({
    {}, # 조건을 비우면 모든 것이 수정됨.
    {"$set":
        {},
    },
)
delete_many({}) # 이것 또한 조건을 비우면 모든 것이 삭제됨.
# client.test.collection.delete_many({"author":"tester"}) # 조건에 맞는 모든 것을 삭제

client.close() # 연결을 끊는 작업이다. 꼭 해주자.

# # 딕셔너리 통째로 넘기기
# new_post = [{},{}]
# coll.insert(new_post)
#
# # 콜렉션 목록 보기
# coll_list = db.collection_names()
# # [u'system.indexes', u'colllection'] ?? 이건 뭐지
#
# # 도큐먼트 하나 가져오기
# onedoc = coll.find_one()
#
# for post in coll.find():
#     pass
# # 도큐먼트 개수 세기
# posts.count()
#
# # 기존 몽고디비 쿼리
# d = datetime.datetime(2009, 11, 12, 12)
# for post in coll.find({'date': {'$lt': d}}).sort('author'):
#     print(post)

# 오늘의 몽고디비는 여기서 마친다.