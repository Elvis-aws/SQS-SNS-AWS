import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


def delete_messages(queue, messages):
    """
    Delete a batch of messages from a queue in a single request.

    :param queue: The queue from which to delete the messages.
    :param messages: The list of messages to delete.
    :return: The response from SQS that contains the list of successful and failed
             message deletions.
    """
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
        logger.exception("Couldn't delete messages from queue %s", queue)
    else:
        return response
