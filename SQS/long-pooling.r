

************
Long-Polling
************
    - This is the option for consumers to wait for messages to arrive in the queue if there are no messages in 
      the queue
    - LongPoling decreases the number of API calls being made
    - LongPooling can be set between 1-20 secs wait
    - This can be enabled at the queue level or at the API level using WaitTimeSeconds
    - This reduces latency as the message is immediately polled by the consumer upon arrival