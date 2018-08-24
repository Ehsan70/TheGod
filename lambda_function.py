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

    logger.info('Received event is : {}'.format(json.dumps(event, indent=2)))

    # todo make this an env variable using cloudformation
    table = dynamodb.Table('GodMessages')
    msgid = event['pathParameters']['msgid']

    response = table.get_item(Key={'MessageId':str(msgid)})
    if 'Item' in response:
        item = response['Item']
    else:
        return result(400, "Msg not found")

    logger.info('Result is : {}'.format(json.dumps(item)))

    return result(200, json.dumps(item))
