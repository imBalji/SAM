import boto3;

class jsonS3:
    s3 = boto3.resource('s3');
    s3Client = boto3.client('s3');

    def readObject(self):
        if(self.fileExist(name="data.json")):
            s3 = self.s3;
            obj = s3.Object("json-data-learnin", "data.json");
            data = obj.get()['Body'].read().decode();
            return data;
        else:
            print("file Doesn't exist!");
            return "File Doesn't exist!";

    def fileExist(self, name):
        client = self.s3Client;
        result = client.list_objects(Bucket="json-data-learnin", Prefix="data.json");
        return 'Contents' in result;