#!/usr/bin/env python3
import os

import aws_cdk as cdk
from LPugensWebCDK.LPugensWebPipeline import LPugensWebPipeline


app = cdk.App()
pipeline = LPugensWebPipeline(
    app, 'LPugensWebPipeline',
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    ),
)

app.synth()
