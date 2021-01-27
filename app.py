#!/usr/bin/env python3

from aws_cdk import core
import time
from gluejob1.As3bucket import HelloCdkStack
from gluejob1.Bgluedatabase import GluedatabaseStack
from gluejob1.Egluejob1_stack import Gluejob1Stack
from gluejob1.Cgluecrawler import GluedemoStack
#from gluejob1.s3assect import s3AssectStack
from gluejob1.Ds3lambda import S3LambdaStack
#from gluejob1.Fworkflow import WF



app = core.App()
HelloCdkStack(app,"As3bucket")
GluedatabaseStack(app, "Bgluedatabase")
Gluejob1Stack(app, "Egluejob1")
GluedemoStack(app, "Cgluecrawler")
S3LambdaStack(app, "Ds3lambda")
#WF(app, "Fworkflow")
#s3AssectStack(app,"s3assect")

app.synth()

