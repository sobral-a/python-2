import uuid
import pymongo

client = pymongo.MongoClient('mongodb://root:root@ds123695.mlab.com:23695/pton2')
todo_items = client.pton2.todo_items

def create(todo_item):
  uid = str(uuid.uuid4())
  todo_items.insert({ '_id': uid, 'text': todo_item, 'done': False})
  return uid
  
def find():
  return list(todo_items.find({}))

def toggle(uid):
  item = todo_items.find_one({'_id': uid})
  todo_items.update_one({ '_id': uid }, {'$set': {'done': not item['done']}})

def remove(uid):
  todo_items.delete_one({'_id': uid})