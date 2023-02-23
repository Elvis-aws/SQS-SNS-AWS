import logging
import boto3
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


def remove_queue(queue):
    """
    Removes an SQS queue. When run against an AWS account, it can take up to
    60 seconds before the queue is actually deleted.

    :param queue: The queue to delete.
    :return: None
    """
    try:
        queue.delete()
        print("Deleted queue with URL=%s.", queue.url)
        logger.info("Deleted queue with URL=%s.", queue.url)
    except ClientError as error:
        logger.exception("Couldn't delete queue with URL=%s!", queue.url)
        raise error
