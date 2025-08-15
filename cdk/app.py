#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.api_stack import ApiStack

env = cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))
app = cdk.App()
ApiStack(app, "api-service-test-dev", env=env, stack_name="api-service-test-dev")
app.synth()
