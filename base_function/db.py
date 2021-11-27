import boto3;
import json;
from json_s3 import jsonS3;

class Database:
    dynamoDB = boto3.resource("dynamodb");

    # Query client and list_tables to see if table exists or not
    def tableExist(self, name):
        # Instantiate your dynamo client object
        client = boto3.client("dynamodb");

        # Get an array of table names associated with the current account and endpoint.
        response = client.list_tables();

        if name in response["TableNames"]:
            return True;
        else:
            return False;
    
    # get all data and return json
    def getItems(self, name):
        s3=jsonS3();
        resp = json.loads(s3.readObject());
        print(resp);

        # Instantiate dynamo resource object
        myDB = self.dynamoDB;

        if(self.tableExist(name=name)):
            data = myDB.Table(name).scan();
            return data["Items"];
        else:
            print("Table doesn't exist.. Reading S3 json to load data onto DynamoDB");
            return {"message":"table doesn't exist"};

    def getItem(self, name, param):
        # Instantiate dynamo resource object
        myDB = self.dynamoDB;

        if(self.tableExist(name=name)):
            data = myDB.Table(name).get_item(Key=param);
            return data;