import json
import boto3
print('Loading function')
glue = boto3.client(service_name='glue', region_name='us-east-1')
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
try:
       glue.start_crawler(Name='nickcrawler')
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
