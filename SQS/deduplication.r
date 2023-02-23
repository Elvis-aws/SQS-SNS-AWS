

****************
De-duplication
****************
    - There is a de-duplication interval of 5 mins
    - This implies the queue will refuse the message with this interval
    *********************
    There are two methods
    *********************
        - Content-based deduplication: this will do a SHA-256 hash on the message body
        - Provide message deduplication id
        **** We can not specify both
    **************
    MessageGroupID
    **************
        - If you specify the same MessageGroupID in an SQS Fifo queue, only one consumer can process all these 
          messages
        - If you specify a different Message Group Id, messages within that group will be in order
        - Each GroupId can have a different customer process the messages
        - Ordering across groups is not a guarantee