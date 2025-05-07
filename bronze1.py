import requests
from pymongo import MongoClient

# connect to MongoDB
mongo_connection_string = "mongodb+srv://injams87:0y4FrO2jR8KBQhkB@cluster0.c356hgh.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(mongo_connection_string)
database = mongo_client["nyc_311"]
collection = database["raw_data"]

# download data in parts
number_of_records_inserted = 0
offset_value = 0
batch_size = 5000

while offset_value < 100000:
    api_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=" + str(batch_size) + "&$offset=" + str(offset_value)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data != []:
            collection.insert_many(json_data)
            print("Inserted " + str(len(json_data)) + " records at offset " + str(offset_value))
            number_of_records_inserted = number_of_records_inserted + len(json_data)
        else:
            print("No data found at offset " + str(offset_value))
    else:
        print("Error getting data at offset " + str(offset_value) + ". Status code: " + str(response.status_code))
    
    offset_value = offset_value + batch_size

print("Finished inserting " + str(number_of_records_inserted) + " records")






