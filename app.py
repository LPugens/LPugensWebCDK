#!/usr/bin/env python3
import aws_cdk as cdk
from LPugensWebCDK.LPugensWebPipeline import LPugensWebPipeline


app = cdk.App()
pipeline = LPugensWebPipeline(
    app, 'LPugensWebPipeline'
)

app.synth()
