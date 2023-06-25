import logging
import boto3
import os
import json
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sns = boto3.client("sns", region_name="eu-west-2")


def s3_sns_trigger(event, context):
    topic_arn = os.getenv('MySNSTopic_Arn')

    try:
        print("Received event: " + json.dumps(event, indent=2))
        message = event['Records'][0]['Sns']['Message']
        print("From SNS: " + message)
        logger.info(
            "S3 delete message from SNS is:", message)
    except ClientError:
        logger.exception("Couldn't read from sns:", topic_arn)
        raise
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{message}",
            }),
        }
