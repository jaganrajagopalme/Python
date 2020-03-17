import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    #https://python.gotrained.com/amazon-s3-boto3/
    s3=boto3.client('s3')
    response=s3.list_buckets()
    #print(response)
    s3.upload_file('Testfile.txt','bucketappslogs','testbucker.txt')
    #print (success)
    return {
        'statusCode': 200
        
    }
