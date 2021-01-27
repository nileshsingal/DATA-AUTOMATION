from aws_cdk import (
    aws_glue as glue,
    aws_iam as iam,
    core
    )
from aws_cdk.aws_stepfunctions_tasks import GlueStartJobRun
import boto3
class Gluejob1Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        client = boto3.client(service_name='glue', region_name='us-east-1',endpoint_url='https://glue.us-east-1.amazonaws.com')

        myJob = client.create_job(Name='sample1', Role='arn:aws:iam::919238404395:role/gluetos3role',
        ExecutionProperty={'MaxConcurrentRuns': 1},
        Command={'Name': 'glueetl','ScriptLocation': 's3://nikhils3/titanicjob.py'})
        
        #myNewJobRun = client.start_job_run(JobName=myJob["Name"])

        #status = glue.get_job_run(JobName='sample1', RunId=["JOB_RUN_ID"])

        #print(status['JobRun']['JobRunState'])
    

