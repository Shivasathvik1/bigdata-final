import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
# Connect to MongoDB
mongo_uri = "mongodb+srv://injams87:0y4FrO2jR8KBQhkB@cluster0.c356hgh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client["nyc_311"]
clean_data = db["clean_data"]


# Fetch cleaned data
data_list = list(clean_data.find())
df = pd.DataFrame(data_list)

# Convert 'created_date' to datetime
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')

# Drop rows where date is invalid
df = df.dropna(subset=['created_date'])

# Extract hour from 'created_date'
df['hour'] = df['created_date'].dt.hour


# Count complaints per hour
hourly_counts = df.groupby('hour').size().reset_index(name='complaint_count')


# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(hourly_counts['hour'], hourly_counts['complaint_count'], color='skyblue')
plt.xticks(hourly_counts['hour'])
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Number of Complaints')
plt.title('Number of Complaints by Hour of Day')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
