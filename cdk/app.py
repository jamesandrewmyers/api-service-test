#!/usr/bin/env python3
import aws_cdk as cdk
from lambda_stack import LambdaStack   # adjust to your file/class

app = cdk.App()
LambdaStack(app, "ApiServiceTestStack", description="API Service Test Stack")
app.synth()
