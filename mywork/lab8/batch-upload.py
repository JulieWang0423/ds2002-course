import boto3
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("s3-batch-upload")

def parse_args():
    if len(sys.argv) < 3:
        print("Usage: python3 batch-upload.py <input-folder> <bucket/prefix>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def upload_files(input_folder, destination):
    if '/' in destination:
        parts = destination.split('/', 1)
        bucket_name = parts[0]
        prefix = parts[1]
    else:
        bucket_name = destination
        prefix = ""

    s3 = boto3.client('s3', region_name='us-east-1')
    
    try:
        files_found = 0
        for filename in os.listdir(input_folder):
            if filename.startswith("results") and filename.endswith(".csv"):
                local_path = os.path.join(input_folder, filename)
                s3_key = os.path.join(prefix, filename)
                s3.upload_file(local_path, bucket_name, s3_key)
                files_found += 1
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return False
    return True

if __name__ == "__main__":
    folder, dest = parse_args()
    success = upload_files(folder, dest)
