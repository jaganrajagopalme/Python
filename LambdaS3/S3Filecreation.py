#Folder creation 
import boto3
import json

def lambda_handler(event,context):
    s3=boto3.client('s3')
    with open('Testfile.txt') as f:
        content=f.read()
    s3.put_object(Body=content,Bucket='bucketappslogs',Key='TestDev/Testfile.txt')
    return {
        'statusCode': 200
        
    }