import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")

        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]

        logger.info(f"Processing file: {key} from bucket: {bucket}")

        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read().decode("utf-8")

        metadata_bucket = bucket + "-processed"
        metadata_key = key + ".metadata.json"
        metadata = {
            "file_name": key,
            "size": response["ContentLength"],
            "bucket": bucket,
        }

        s3_client.put_object(
            Bucket=metadata_bucket,
            Key=metadata_key,
            Body=json.dumps(metadata),
        )

        logger.info(f"Metadata stored at {metadata_bucket}/{metadata_key}")

        return {"statusCode": 200, "body": "File processed successfully"}

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise e
