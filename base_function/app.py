import json;
import boto3;
from db import Database;

def lambda_handler(event, context):
    
    print(event);
    dynamodb = boto3.resource("dynamodb");
    
    if(event["httpMethod"]=="GET"):
        myDB = Database();
        if(event["queryStringParameters"]==None):
            data = myDB.getItems(name="Student");
            return {
                "statusCode": 200,
                "body": json.dumps(data)
            };
        else:
            data = myDB.getItem(name="Student", param=event["queryStringParameters"]);
            return {
                "statusCode": 200,
                "body": json.dumps(data)
            };

    elif(event["httpMethod"]=="POST"):
            
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                    "message": "either GET or POST methods are allowed"
                })
        };