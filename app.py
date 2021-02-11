#!/usr/bin/env python3

from aws_cdk import core

from high_available_webapp.high_available_webapp_stack import HighAvailableWebappStack


app = core.App()
HighAvailableWebappStack(app, "high-available-webapp", env={'region': 'us-west-2'})

app.synth()
