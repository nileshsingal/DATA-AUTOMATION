from aws_cdk import (aws_s3 as s3,aws_glue as glue,core)

class GluedatabaseStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        dbdemo = glue.Database(self,"nikhildb", database_name="nike")