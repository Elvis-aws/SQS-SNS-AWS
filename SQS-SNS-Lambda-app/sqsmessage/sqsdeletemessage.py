import logging
import boto3
import os
from botocore.exceptions import ClientError
sqs = boto3.client("sqs", region_name="eu-west-2")
logger = logging.getLogger(__name__)


def delete_message(event, context):
    queue_url = os.getenv('SQSqueueName')
    try:
        message = sqs.receive_messages(
            QueueUrl=queue_url,
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        )
        message.delete()
        logger.info("Deleted message: %s", message.message_id)
    except ClientError as error:
        logger.exception("Couldn't delete message: %s", message.message_id)
        raise error


def delete_messages(queue, messages):
    try:
        entries = [{
            'Id': str(ind),
            'ReceiptHandle': msg.receipt_handle
        } for ind, msg in enumerate(messages)]
        response = queue.delete_messages(Entries=entries)
        if 'Successful' in response:
            for msg_meta in response['Successful']:
                logger.info("Deleted %s", messages[int(msg_meta['Id'])].receipt_handle)
        if 'Failed' in response:
            for msg_meta in response['Failed']:
                logger.warning(
                    "Could not delete %s",
                    messages[int(msg_meta['Id'])].receipt_handle
                )
    except ClientError:
        logger.exception("Couldn't delete snsmessage from queue %s", queue)
    else:
        return response