from pymongo import MongoClient
from system import conf

client = MongoClient(conf.mongo['host'],conf.mongo['port'])

db = client.test
#collection = db.hoge
collection = db.masters

for m in collection.find():
  print(m)

'''
def find_all_test():
  print 'found >>>'
  for m in collection.find():
    print m
  return collection.find()

def find_with_condition_test(condi):
  print 'found by condition >>>'
  for m in collection.find(condi):
    print m
  return collection.find(condi)

def insert_test(k_v_obj):
  print 'inserted >>>'
  res = collection.insert(k_v_obj)
  print res
  return res

def update_test(mongo_obj):
  print 'updated >>>'
  res = collection.save(mongo_obj)
  print res
  return res

def initialize():
  print 'initialize test!!'
  all_member = collection.find()
  for m in all_member:
    print collection.remove(m)

if __name__ == '__main__':

  initialize()

  # insert new
  rit = {'name' : 'Ritsu', 'birthday' : '08-21'}
  mio = {'name' : 'Mio',   'birthday' : '01-15'}
  insert_test(rit)
  insert_test(mio)

  find_all_test()

  # insert new
  yui = {'name' : 'Yui',   'birthday' : '11-27'}
  mug = {'name' : 'Mugi',  'birthday' : '07-02'}
  azu = {'name' : 'Azu',   'birthday' : '11-11'}
  insert_test(yui)
  insert_test(mug)
  insert_test(azu)

  found_member = find_all_test()

  for m in found_member:
    if m['name'] == 'Ritsu':
      m['is_my_wife'] = True
      # update
      update_test(m)

  find_all_test()

  # find by condition
  find_with_condition_test({'is_my_wife':True})
'''
