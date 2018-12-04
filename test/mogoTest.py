from pymongo import MongoClient



client = MongoClient("mongodb://localhost:27017")
dblist = client.list_database_names()
print(dblist)

mydb = client['mydb']
myContact = mydb['contact']
contact1={'firstname':'Andy', 'lastname': 'Qin', 'age': 32, 'telephone': '13571806472'}
# contact1_id = myContact.insert_one(contact1)
# print(client.list_database_names())
# print(contact1_id)

contact_list = [{'firstname':'Tons', 'lastname': 'Wang', 'age': 27, 'telephone': '1234'},
                {'firstname':'Bala', 'lastname': 'Bi', 'age': 26, 'telephone': '1890'}
                ]

# lists_result = myContact.insert_many(contact_list)
# # print("inset result ids", lists_result)

x = myContact.find_one()
print("x type is", type(x))
print(x)
print("******************************")
contacts = myContact.find()
for c in contacts:
    print(c)

print("******************************")

for f in myContact.find({},{"_id":0,'firstname':1, 'lastname': 1}):
    print(f)
print("******************************")

myQuery = myContact.find({"firstname":{"$lt":"H"}})
for m in myQuery:
    print(m)
print("******************************")
limitQuery = myContact.find().limit(2)
for l in limitQuery:
    print(l)

print("*************Update*****************")
myQuery = {"firstname": 'AndyNew'}
newValue = {"$set": {'firstname': 'AndyNew1'}}
x = myContact.update_one(myQuery,newValue)
print(x.modified_count, x.matched_count)
for v in myContact.find():
    print(v)