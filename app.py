#!/usr/bin/env python3

from aws_cdk import core


from pipelines_webinar.pipeline_stack import PipelineStack



app = core.App()
PipelineStack(app, 'PipelineStack', env={
    'account': '881299606849',
    'region': 'us-east-1'
})
app.synth()