

*****************
Dead-Letter-Queue
*****************
    - If a consumer can not process a message, the message goes back into the queue
    - This can go on and on if the message has a problem i.e a no ending loop of reading and back in the queue
    - The MaximumReceives thresh hold can be set and the message will be moved into a dead letter queue
    - This is were an application or someone can determine the cause of the read failure
    - Always set the max retention period (14 days) for the dead letter queue to avoid messages from expiring
    ********
    Re-drive
    ********
        - You can configure a dead-letter queue re-drive to move standard unconsumed messages out of an existing
          dead-letter queue back to their source queues
        - Amazon SQS supports dead-letter queue re-drive only for standard queues in the Amazon SQS console
        - Amazon SQS doesnt support filtering and modifying messages while re-driving them from the dead-letter
          queue
        - A dead-letter queue re-drive task can run a maximum of 36 hours
        - Amazon SQS supports a maximum of 100 active re-drive tasks per account
        - A new messageID and enqueueTime are assigned to re-driven messages