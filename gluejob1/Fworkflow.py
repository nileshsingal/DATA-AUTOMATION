from aws_cdk import (
    aws_glue as glue,
    aws_iam as iam,
    core
    )
from aws_cdk.aws_stepfunctions_tasks import GlueStartJobRun
import boto3
import sys

class WF(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)
        
        client = boto3.client(service_name='glue', region_name='us-east-1',
                              endpoint_url='https://glue.us-east-1.amazonaws.com')
        
        myworkflow = client.create_workflow(Name='nikhil1')
                    
        gluetrig = client.create_trigger(
            Name='gluetrigger',
            WorkflowName='nikhil1',
            Type= 'CONDITIONAL',
            Predicate={
                'Logical': 'AND',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'CrawlerName': 'nickcrawler',
                        'CrawlState': 'SUCCEEDED'
                    },
                ]
            },
            Actions=[
                {
                    'JobName': 'sample1',
                    'Timeout': 123,
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                },
            ],
            StartOnCreation=True

            
        )
