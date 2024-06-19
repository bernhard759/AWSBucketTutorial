from dotenv import load_dotenv
import boto3
import os
import csv

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

# Get the CSV file from S3
obj = s3.get_object(Bucket=bucket_name, Key=file_name)
data = obj['Body'].read().decode('utf-8').splitlines()[1:]  # Skip the header row

# Read the CSV data
reader = csv.reader(data)
for row in reader:
    print(row)
