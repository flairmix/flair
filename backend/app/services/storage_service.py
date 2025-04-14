import os
from typing import BinaryIO

import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

BUCKET_NAME = "dwg-files"
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://minio:9000")
S3_REGION = os.getenv("S3_REGION", "us-east-1")
S3_ACCESS_KEY = os.getenv("MINIO_ROOT_USER", "admin")
S3_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD", "password")

s3_client = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    region_name=S3_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)

def upload_file(file_obj: BinaryIO, filename: str, content_type: str = "application/octet-stream") -> None:
    s3_client.upload_fileobj(
        Fileobj=file_obj,
        Bucket=BUCKET_NAME,
        Key=filename,
        ExtraArgs={"ContentType": content_type}
    )

def download_file(filename: str) -> bytes:
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
    return response["Body"].read()

def generate_presigned_url(filename: str, expires_in: int = 3600) -> str:
    return s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": filename},
        ExpiresIn=expires_in,
    )

def list_files() -> list[str]:
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    contents = response.get("Contents", [])
    return [obj["Key"] for obj in contents]

def delete_file_by_name(filename: str) -> None:
    s3_client.delete_object(Bucket=BUCKET_NAME, Key=filename)
