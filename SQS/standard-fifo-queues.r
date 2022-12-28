

**************
Standard-Queue
**************
    - Amazon SQS offers standard as the default queue type
    - They support a nearly unlimited number of API calls per second, per API action (SendMessage, 
      ReceiveMessage, or DeleteMessage)
    - They support at-least-once message delivery
    - However, occasionally (because of the highly distributed architecture that allows nearly unlimited throughput), 
      more than one copy of a message might be delivered out of order
    - They provide best-effort ordering which ensures that messages are generally delivered in the same order as 
      theyre sent
************
Fifo-Queueus
************
    - FIFO (First-In-First-Out) queues have all the capabilities of the standard queues, but are designed to 
      enhance messaging between applications when the order of operations and events is critical, or where duplicates 
      cant be tolerated
    - They also provide exactly-once processing, but have a limited number of transactions per second (TPS)
    - You can use Amazon SQS high throughput mode with your FIFO queue to increase your transaction limit
    - Limited throughput due to the ordering constrain
    - 300 msg/s without batching and 3000 msg/s with batching
    - Exactly-once send capability (by removing duplicates)
    - Queue naming should end with .fifo
    - Message group ID: This specifies a message belongs to a particular group
    - Message deduplication ID: The token used for deduplication messages within the deduplication interval
    - Content-based deduplication: this will set message id to optional when enabled