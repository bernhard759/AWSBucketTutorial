from dotenv import load_dotenv
import boto3
import os

# Load environment variables from .env file
load_dotenv()

# Create a Boto3 session with the credentials from the .env file
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

# Create an S3 client from the session
s3 = session.client('s3')


# Define the bucket and file names
bucket_name = 'mytestingbucket1bg'
file_name = 'dummydata.csv'

# Create a list of dictionaries with your data
data = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'},
]

# Create a CSV file in memory
csv_file = ','.join(data[0].keys()) + '\n'
for row in data:
    csv_file += ','.join([str(value) for value in row.values()]) + '\n'

# Upload the CSV file to S3
s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_file)
print(f'CSV file uploaded to S3 bucket: {bucket_name}/{file_name}')
