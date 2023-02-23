

******************
The Fanout Pattern
******************
    - This is when a message published to an SNS topic is replicated and pushed to multiple endpoints, such as 
      Kinesis Data Firehose delivery streams, Amazon SQS queues, HTTP(S) endpoints, and Lambda functions
    - This allows for parallel asynchronous processing
    - Push one message onto an SNS topic and two SQS queues will subscribe to the topic
    - No data loss
    - Make sure SQS queue access policy allows for SNS to write
    - We can have both standard and Fifo queues as subscribers
    