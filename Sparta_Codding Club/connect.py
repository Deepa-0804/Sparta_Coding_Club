from pymongo import MongoClient
client = MongoClient('mongosh "mongodb+srv://cluster1.n9cs5ny.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509" --apiVersion 1 --tls --tlsCertificateKeyFile <path to PEM file>')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)


# Insert {'name':'bobby','age':21} in the collection called'users'.
db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})


# View all data in MongoDB
all_users = list(db.users.find({},{'id':False}))

print(all_users[0])         # Show 0th result
print(all_users[0]['name']) # Show'name' of 0th result

for user in all_users:      # loop through and see all results
    print(user)


    user = db.users.find_one({'name':'bobby'})
print(user)

# Example-There are many typos, so let's copy this line!
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)


# Save-example
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# Find one-example
user = db.users.find_one({'name':'bobby'})

# Find multiple-example
same_ages = list(db.users.find({'age':21},{'_id':False}))

# Replace-example
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# Clear-example
db.users.delete_one({'name':'bobby'})