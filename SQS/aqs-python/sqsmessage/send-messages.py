import logging
import boto3
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


def send_messages(queue, messages):
    """
    Send a batch of messages in a single request to an SQS queue.
    This request may return overall success even when some messages were not sent.
    The caller must inspect the Successful and Failed lists in the response and
    resend any failed messages.

    :param queue: The queue to receive the messages.
    :param messages: The messages to send to the queue. These are simplified to
                     contain only the message body and attributes.
    :return: The response from SQS that contains the list of successful and failed
             messages.
    """
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
        logger.exception("Send messages failed to queue: %s", queue)
        raise error
    else:
        return response
