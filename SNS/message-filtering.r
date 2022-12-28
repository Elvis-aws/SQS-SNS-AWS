
*****************
Message Filtering
*****************
   - Json policy used in filtering messages sent to subscribers of an SNS topic
   - No filtering implies all messages will be received
   - The following example shows a message payload sent by an Amazon SNS topic that publishes customer transactions. 
     The MessageAttributes field includes attributes that describe the transaction
   {
      "Type": "Notification",
      "MessageId": "a1b2c34d-567e-8f90-g1h2-i345j67klmn8",
      "TopicArn": "arn:aws:sns:us-east-2:123456789012:MyTopic",
      "Message": "message-body-with-transaction-details",
      "Timestamp": "2019-11-03T23:28:01.631Z",
      "SignatureVersion": "4",
      "Signature": "signature",
      "UnsubscribeURL": "unsubscribe-url",
      "MessageAttributes": {
         "customer_interests": {
            "Type": "String.Array",
            "Value": "[\"soccer\", \"rugby\", \"hockey\"]"
         },
         "store": {
            "Type": "String",
            "Value":"example_corp"
         },
         "event": {
            "Type": "String",
            "Value": "order_placed"
         },
         "price_usd": {
            "Type": "Number", 
            "Value": "210.75"
         }
      }
   }