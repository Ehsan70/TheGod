import boto3
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')

def result(status, message):
    return {
        'statusCode': status,
        'body': message,
        'headers': {
            'Content-Type': 'application/json'
        },
    }


def lambda_handler(event, context):

    print('Received event is : {}'.format(json.dumps(event, indent=2)))

    # todo make this an env variable using cloudformation
    table = dynamodb.Table('GodMessages')
    # msgid the url parameter passed to API gateway. All the URL paramteres ap pear under pathParameters
    msgid = event['pathParameters']['msgid']

    response = table.get_item(Key={'MessageId':str(msgid)})
    if 'Item' in response:
        # If there is an Item key in that response then we have found the item
        item = response['Item']
    else:
        # If there is no Item key in the response then we have not found the item
        return result(400, "Msg not found")

    logger.info('Result is : {}'.format(json.dumps(item)))

    return result(200, json.dumps(item))
