import json
import logging
import boto3
import os
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sns = boto3.client("sns", region_name="eu-west-2")


def publish_message(event, context):

    topic_arn = os.getenv('MySNSTopic_Arn')
    payload = json.loads(event['body'])
    message_body = payload['message']
    message_attributes = payload['attribute']

    try:
        att_dict = {}
        for key, value in message_attributes.items():
            if isinstance(value, str):
                att_dict[key] = {'DataType': 'String', 'StringValue': value}
            elif isinstance(value, bytes):
                att_dict[key] = {'DataType': 'Binary', 'BinaryValue': value}
        response = sns.publish(
            TargetArn=topic_arn,
            Message=message_body,
            MessageAttributes=att_dict
        )
        message_id = response['MessageId']
        logger.info(
            "Published message with attributes %s to topic %s.", message_attributes, topic_arn)
    except ClientError:
        logger.exception("Couldn't publish message to topic %s.", topic_arn)
        raise
    else:
        return message_id