import boto3
s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'ds2002-dsy4qx'
local_file = 'flower.jpg'
s3_key = 'flower.jpg'
s3.upload_file(local_file, bucket_name, s3_key)
print("Success")