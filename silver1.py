import pandas as pd
from pymongo import MongoClient

# 1 Connect to MongoDB
connection_string = "mongodb+srv://injams87:0y4FrO2jR8KBQhkB@cluster0.c356hgh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# Select database and collection
db = client["nyc_311"]
raw_data = db["raw_data"]


# 2 Get raw data from MongoDB
# Find all documents and put them in a list
raw_data_list = []
for doc in raw_data.find():
    raw_data_list.append(doc)

# Create a DataFrame from the list of documents
df = pd.DataFrame(raw_data_list)


# 3 Remove rows with missing complaint_type or created_date

df_no_missing = df.dropna(subset=['complaint_type', 'created_date'])


# 4 Define columns we want to check for duplicates
columns_to_check = [
    'unique_key',
    'created_date',
    'closed_date',
    'agency',
    'complaint_type',
    'descriptor',
    'borough'
]

# 5  Remove duplicate rows based on those columns
df_no_duplicates = df_no_missing.drop_duplicates(subset=columns_to_check)


# 6 Keep only the columns we want
final_df = df_no_duplicates[columns_to_check]


# 7 Print info about cleaned data
row_count = final_df.shape[0]
column_count = final_df.shape[1]
print("Cleaned data has", row_count, "rows and", column_count, "columns")


# 8 Write cleaned data to MongoDB clean_data collection
clean_data = db["clean_data"]

# (Optional) Clear old data in clean_data collection
clean_data.delete_many({})

# Insert cleaned data into clean_data collection
clean_data.insert_many(final_df.to_dict("records"))

print("Cleaned data written to MongoDB collection 'clean_data'")


# 9 Show first few rows of cleaned data
print(final_df.head())




