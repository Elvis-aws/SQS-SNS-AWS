

**************************
Message visibility timeout
**************************
    - After a message is pulled or viewed by a consumer, it becomes invisible from other consumers 
    - Visibility timeout is 30 seconds by default
    - The message will be returned to the queue if its not consumed and deleted in this time period
    - If the message is not consumed it might be consumed twice
    - If a consumer can not consume a message in the 30 seconds time period, then use the ChangeMessageVisibility
      API to change this
        - visibility timeout with a meaningful timeout.
        - You can also set this visibility timeout on the console
    