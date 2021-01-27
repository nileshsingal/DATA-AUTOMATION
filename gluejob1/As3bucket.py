from aws_cdk import (
    aws_s3 as s3,
    core 
)

class HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "nikhil420", bucket_name="mybucketnikhil420demo",public_read_access=True,website_index_document="index.html")

