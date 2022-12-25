import json
import logging
import boto3
import os
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sqs = boto3.client("sqs", region_name="eu-west-2")


def send_message(event, context):
    queue_url = os.getenv('SQSqueueName')
    _delaySeconds = 10
    payload = json.loads(event['body'])
    message_body = payload['message']
    message_attributes = payload['attribute']

    if not message_attributes:
        message_attributes = {}

    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body,
            DelaySeconds=_delaySeconds,
            MessageAttributes=message_attributes
        )
    except ClientError as error:
        logger.exception("Send message failed: %s", message_body)
        raise error
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{response}",
            }),
        }


def send_messages(queue, messages):
    try:
        entries = [{
            'Id': str(ind),
            'MessageBody': msg['body'],
            'MessageAttributes': msg['attributes']
        } for ind, msg in enumerate(messages)]
        response = queue.send_messages(Entries=entries)
        if 'Successful' in response:
            for msg_meta in response['Successful']:
                logger.info(
                    "Message sent: %s: %s",
                    msg_meta['MessageId'],
                    messages[int(msg_meta['Id'])]['body']
                )
        if 'Failed' in response:
            for msg_meta in response['Failed']:
                logger.warning(
                    "Failed to send: %s: %s",
                    msg_meta['MessageId'],
                    messages[int(msg_meta['Id'])]['body']
                )
    except ClientError as error:
        logger.exception("Send snsmessage failed to queue: %s", queue)
        raise error
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{response}",
            }),
        }
