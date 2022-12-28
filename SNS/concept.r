
**********
Amazon SNS
**********
    - Amazon SNS is a managed service that provides message delivery from publishers to subscribers (also known 
      as producers and consumers)
    - Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical 
      access point and communication channel
    - Clients can subscribe to the SNS topic and receive published messages using a supported endpoint type, such 
      as 
        - Amazon Kinesis Data Firehose
        - Amazon SQS
        - AWS Lambda
        - HTTP(S)
        - Email
        - Mobile push notifications
        - Mobile text messages (SMS).
    - One message and many receivers
    - Producers send messages to a topic
    - Subscribers subscribe to the topic and receive messages
    - up to 125,00,000 subscriptions per topic
    - Up to 100,000 topic limits
    - We can create both a Standard and Fifo SNS topics
