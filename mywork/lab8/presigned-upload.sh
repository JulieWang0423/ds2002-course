#!/bin/bash
FILE_NAME=$1
BUCKET_NAME=$2
EXPIRATION=$3
echo "Uploading $FILE_NAME to s3://$BUCKET_NAME..."
python3 -m awscli s3 cp "$FILE_NAME" "s3://$BUCKET_NAME/$FILE_NAME"
echo "Generating presigned URL valid for $EXPIRATION seconds..."
python3 -m awscli s3 presign "s3://$BUCKET_NAME/$FILE_NAME" --expires-in "$EXPIRATION"