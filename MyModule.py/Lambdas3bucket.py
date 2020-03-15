import boto3
import json

s3=boto3.resource('s3')
def lambda_handler(event,context):
    bucketlist=[]
    for bucketname in s3.buckets.all():
        
        bucketlist.append(bucketname.name)
        return {
            'statuscode':200,
            'body': bucketlist

        }