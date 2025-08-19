#!/usr/bin/env python3
import aws_cdk as cdk
from lambda_stack import LambdaStack

app = cdk.App()
LambdaStack(app, "ApiServiceTestStack")
app.synth()