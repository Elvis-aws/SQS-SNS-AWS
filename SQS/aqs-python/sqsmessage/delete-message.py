import logging
import sys
import boto3
from botocore.exceptions import ClientError
sqs = boto3.resource('sqs')
logger = logging.getLogger(__name__)


def delete_message(queue_name):
    """
    Delete a message from a queue. Clients must delete messages after they
    are received and processed to remove them from the queue.

    :param message: The message to delete. The message's queue URL is contained in
                    the message's metadata.
    :return: None
    """
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    try:
        message = queue.receive_messages(
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        )
        message.delete()
        logger.info("Deleted message: %s", message.message_id)
    except ClientError as error:
        logger.exception("Couldn't delete message: %s", message.message_id)
        raise error

delete_message('DemoS3Notification')