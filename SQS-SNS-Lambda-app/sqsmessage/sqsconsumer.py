import logging
import boto3
import os
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
sqs = boto3.client("sqs", region_name="eu-west-2")


def sqs_consumer(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))


def receive_messages(event, context):
    wait_time = 5
    max_number = event['queryStringParameters']['snsmessage']
    queue_url = os.getenv('SQSqueueName')
    try:
        messages = sqs.receive_messages(
            QueueUrl=queue_url,
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=max_number,
            WaitTimeSeconds=wait_time
        )
        for msg in messages:
            print("Received message: %s: %s", msg.message_id, msg.body)
    except ClientError as error:
        logger.exception("Couldn't receive snsmessage from queue: %s", queue_url)
        raise error
    else:
        return messages
