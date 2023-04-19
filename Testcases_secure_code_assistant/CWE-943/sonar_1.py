import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

config = Config(
    region_name = 'your_region',
    signature_version = 'v4',
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username:str, password:str) -> dict:
    '''
    get the user information from users table by using username and password
    '''
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': username},
                'password': {'S': password}
            }
        )
        return response['Item']
    except ClientError as e:
        print(e.response['Error']['Message'])