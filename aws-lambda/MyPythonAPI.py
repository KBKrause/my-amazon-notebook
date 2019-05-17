import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getCat(event, context):
    return {
        'statusCode': 200,
        'catName': 'Toffee'
    }