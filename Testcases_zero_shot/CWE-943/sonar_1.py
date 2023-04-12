import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username,password):
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
        item = response['Item']
        user_info = {
            'username': item['username']['S'],
            'password': item['password']['S'],
            'email': item['email']['S']
        }
        return user_info
    except Exception as e:
        print(e)
        return None