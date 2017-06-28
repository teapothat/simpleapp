from pymongo import MongoClient, TEXT
import json
import os


source = ""

def download_data(source=source):
	import requests
	with open('scripts/data.json', 'w') as data_file:
		response = requests.get(source)
		data_file.write(response.content)

def load_data():
	if not os.path.isfile('scripts/data.json'):
		download_data()

	with open('scripts/data.json') as data_file:
		return json.loads(data_file.read())


def update_item_if_not_exist(collection, item):
	key = {'_id': item["id"]}
	del item["id"]
	data = item
	collection.update(key, data, upsert=True);


def upload_to_mongodb(data):
    # Connect to db
    client = MongoClient()
    db = client.simpleapp
    collection = db.doodles

    for item in data:
        update_item_if_not_exist(collection, item)

    collection.create_index([("description" , TEXT),("title", TEXT)], name="search_index")



if __name__ == "__main__":

	data = load_data()
	upload_to_mongodb(data)

	print "Finsihed"

