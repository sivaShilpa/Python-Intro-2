import boto3
import logging

sqs = boto3.client('sqs')


def send_message_to_sqs(cat, url):
    response = sqs.send_message(
        QueueUrl=url,
        DelaySeconds=10,
        MessageAttributes={
            'PetName': {
                'DataType': 'String',
                'StringValue': cat['cat_name']
            },
            'PetId': {
                'DataType': 'Number',
                'StringValue': str(cat['cat_id'])
            },
            'Status': {
                'DataType': 'String',
                'StringValue': cat['status']
            }
        },
        MessageBody=('body')
    )
    return response['MessageId']


def read_message_from_sqs(url):
    retval = None

    # Read message from SQS queue.
    response = sqs.receive_message(
        QueueUrl=url,
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )

    message = None
    try:
        message = response['Messages'][0]  # Only read one.
    except KeyError as ke:
        logging.info("SQS queue is empty.")

    if message:
        retval = {
            "Status": message["MessageAttributes"]["Status"]["StringValue"],
            "PetId": message["MessageAttributes"]["PetId"]["StringValue"],
            "PetName": message["MessageAttributes"]["PetName"]["StringValue"],
        }

        # Delete message once we have read it from the queue.
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=url,
            ReceiptHandle=receipt_handle
        )

    return retval
