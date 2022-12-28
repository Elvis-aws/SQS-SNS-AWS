
*******************
SQS access policies
*******************
    - Cross-account access to SQS
      - Allowing other services to write to SQS
*************
Access policy
*************
    - Define who can send/receive messages to the queue
        - Only the queue onwner
        - Only the specified account, IAM users and roles
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
        "AWS": "696685998805"
      },
      "Action": [
        "SQS:*"
      ],
      "Resource": "arn:aws:sqs:eu-west-2:696685998805:demoqueue"
    }
  ]
}