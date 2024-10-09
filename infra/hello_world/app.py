import json # import modules
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    # Get the current visit count
    response = table.get_item(
        Key={
            'ID': 'visits'
        }
    )
    
    visit_count = response['Item']['counter']
    visit_count = int(visit_count) + 1
    
    # Update the visit count in DynamoDB
    table.put_item(
        Item={
            'ID': 'visits',
            'counter': visit_count
        }
    )
    
    # Return the updated visit count as JSON
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({'counter': visit_count})
    }
