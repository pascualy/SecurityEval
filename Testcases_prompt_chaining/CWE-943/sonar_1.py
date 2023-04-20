import boto3
import os

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    '''
    get the user information from users table by using username and password
    '''
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['USERS_TABLE'])
    response = table.get_item(
        Key={
            'username': username,
            'password': password
        }
    )
    return response.get('Item')