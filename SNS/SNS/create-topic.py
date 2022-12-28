import json
import logging
import time
import boto3
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)


# Create SNS Topic
def create_topic(name):
    sns_resource = boto3.resource('sns')
    try:
        topic = sns_resource.create_topic(Name=name)
        logger.info("Created topic %s with ARN %s.", name, topic.arn)
    except ClientError:
        logger.exception("Couldn't create topic %s.", name)
        raise
    else:
        return topic

create_topic('my-s3-notifications')