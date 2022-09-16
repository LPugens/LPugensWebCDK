#!/usr/bin/env python3
import aws_cdk as cdk
from LPugensWebCDK.LPugensWebPipeline import LpugensWebPipeline


app = cdk.App()
pipeline = LpugensWebPipeline(
    app, 'LPugensWebPipeline'
)

app.synth()
