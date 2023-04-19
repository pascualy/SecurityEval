import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
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
        user = response['Item']
        return user
    except Exception as e:
        print(f"Error getting user: {e}")
        return None