import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

CORS_HEADERS = {
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*'
}

def lambda_handler(event, context):
    try:
        # Atomically increment the counter and return the new value
        response = table.update_item(
            Key={'ID': 'visits'},
            UpdateExpression='ADD #counter :increment',
            ExpressionAttributeNames={'#counter': 'counter'},
            ExpressionAttributeValues={':increment': 1},
            ReturnValues='UPDATED_NEW'
        )
        visit_count = int(response['Attributes']['counter'])
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'headers': CORS_HEADERS,
        'body': json.dumps({'counter': visit_count})
    }
