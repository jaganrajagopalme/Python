import boto3
import json
dynamodb= boto3.resource('dynamodb')
tables= dynamodb.Tables('BookList')
def lambda_handler(event,context):
    response=tables.put_item(Key={'BookId':'34','Author':'Jagan','BookName':'StartupIdeas'})
    return response {
        'statusCode':200,
        'body': response
    }
