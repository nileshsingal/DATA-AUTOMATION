from aws_cdk import (
    aws_s3 as s3,
    core ,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins

    )
import os.path
dirname = os.path.dirname("C:/")
from aws_cdk.aws_s3_assets import Asset
from aws_cdk.aws_glue import CfnJob


class s3AssectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # website_bucket = s3.Bucket(self, "mybucketnikhil",bucket_name="nikhilramgiri420",website_index_document="index.html",public_read_access=True)

        asset = Asset(self, 'SampleSingleFileAsset',path=os.path.join("Project_Data",'Titanic.csv'))

        bucketname = core.CfnOutput(self, "S3Bucket", value=asset.s3_bucket_name,description="mynameisnikhil420",export_name="nikhil420")
        core.CfnOutput(self, "S3ObjectKey", value=asset.s3_object_key,description="Titanic")
        core.CfnOutput(self, "S3HttpURL", value=asset.http_url)
        core.CfnOutput(self, "S3ObjectURL", value=asset.s3_object_url)
        
    
        

    