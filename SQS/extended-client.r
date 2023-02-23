

*******************
SQS Extended Client
*******************
    - This client library helps us send messages that are greater than 256 kb
    - Its a Java library and can be implemented in many languages
    - The large message will be stored in S3, this client library will create meta-data message pointers and 
      insert them into the queue pointing to the large message in the bucket
    - When the consumer reads the small meta-data messages, they will be re-directed to read the large messages 
      in the S3 bucket