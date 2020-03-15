import json
import boto3
dynamodb= boto3.resource('dynamodb')
table = dynamodb.Table('BookList')
def lambda_handler(event,context):
    response= table.get_item(Key={"BookId":"2"})
    print(response)
    return {
        'statuscode':200,
        'body': response
    }
    