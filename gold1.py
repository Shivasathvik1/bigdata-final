import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
my_connection_string = "mongodb+srv://injams87:0y4FrO2jR8KBQhkB@cluster0.c356hgh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(my_connection_string)

# Choose database and collection
db = client["nyc_311"]
collection = db["clean_data"]

# Create aggregation to count complaints per borough
borough_aggregation = [
    {"$group": {"_id": "$borough", "complaint_count": {"$sum": 1}}},
    {"$project": {"borough": "$_id", "complaint_count": 1, "_id": 0}}
]
borough_result = collection.aggregate(borough_aggregation)

# Convert aggregation result to DataFrame
borough_data = []
for item in borough_result:
    borough_data.append(item)
df_borough = pd.DataFrame(borough_data)

# Create aggregation to count complaints per complaint_type
complaint_aggregation = [
    {"$group": {"_id": "$complaint_type", "complaint_count": {"$sum": 1}}},
    {"$project": {"complaint_type": "$_id", "complaint_count": 1, "_id": 0}}
]
complaint_result = collection.aggregate(complaint_aggregation)

# Convert complaint aggregation to DataFrame
complaint_data = []
for item in complaint_result:
    complaint_data.append(item)
df_complaint = pd.DataFrame(complaint_data)

# Add a column to say which type of aggregation this is
df_borough["type"] = "borough"
df_borough = df_borough.rename(columns={"borough": "category"})

df_complaint["type"] = "complaint_type"
df_complaint = df_complaint.rename(columns={"complaint_type": "category"})

# Make sure both have same column order
df_borough = df_borough[["type", "category", "complaint_count"]]
df_complaint = df_complaint[["type", "category", "complaint_count"]]

# Combine both DataFrames into one
combined_data = pd.concat([df_borough, df_complaint], ignore_index=True)

# Save combined data to CSV
combined_data.to_csv("gold_aggregated_data.csv", index=False)

print("Done! Aggregated data saved to gold_aggregated_data.csv")





