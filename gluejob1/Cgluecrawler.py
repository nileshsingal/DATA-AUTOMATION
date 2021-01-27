from aws_cdk import (aws_s3 as s3,aws_glue as glue,core)

class GluedemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        glue_trigger = glue.CfnTrigger(self, "gluetrigger",
            name = "etl-trigger",
            type="ON_DEMAND",schedule=None,
            actions=[
                {
                    "jobName": "glue_crawler"
                }
            ]
        )



        glue_crawler = glue.CfnCrawler(self, 'glue-crawler-id',description="Glue Crawler for my-data-science-s3",
        name='nickcrawler',database_name='nike',schedule=None,role='arn:aws:iam::919238404395:role/service-role/AWSGlueServiceRole-my_2nd_iamrole',
        targets={"s3Targets": [{"path": "s3://nikhils3/file/Titanic.csv"}]})

        glue_trigger.add_depends_on(glue_crawler)
