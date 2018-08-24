from __future__ import print_function
import boto3
import json

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
    print('Received event is : '+ json.dumps(event))

    # todo make this an env variable using cloudformation
    table = dynamodb.Table('GodMessages')

    if (event['resource'] == "/messages"):
        response = table.scan()
        print('Response from scan is : ' + json.dumps(response))
        if "ResponseMetadata" in response:
            del response["ResponseMetadata"]
        return {
            'statusCode': '200',
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    elif (event['resource'] == "/messages/{msgid}" and event['httpMethod'] == "GET"):
        # msgid the url parameter passed to API gateway. All the URL paramteres ap pear under pathParameters
        msgid = event['pathParameters']['msgid']
        print('Getting the message with ID {}.'.format(msgid))
        response = table.get_item(Key={'MessageId':str(msgid)})
        print('Response from get_item is : ' + json.dumps(response))
        if 'Item' in response:
            # If there is an Item key in that response then we have found the item
            item = response['Item']
        else:
            # If there is no Item key in the response then we have not found the item
            return result(400, "Msg not found")

        print('Constructed result is : ' + json.dumps(item))
        return result(200, json.dumps(item))
    else:
        return result(500, "The resource {} is no handled by lambda.".format(event['resource']))

    