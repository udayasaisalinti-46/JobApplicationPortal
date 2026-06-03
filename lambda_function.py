import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JobApplications')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    required_fields = [
        'fullName',
        'email',
        'phoneNumber',
        'qualification',
        'experience',
        'skills',
        'coverLetter'
    ]

    for field in required_fields:
        if field not in body or body[field] == "":
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'message': f'{field} is required'
                })
            }

    application_id = str(uuid.uuid4())

    item = {
        'applicationId': application_id,
        'fullName': body['fullName'],
        'email': body['email'],
        'phoneNumber': body['phoneNumber'],
        'qualification': body['qualification'],
        'experience': body['experience'],
        'skills': body['skills'],
        'coverLetter': body['coverLetter'],
        'appliedDate': datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Application Submitted Successfully',
            'applicationId': application_id
        })
    }
