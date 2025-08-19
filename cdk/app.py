from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class ApiServiceTestStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(
            self, "ApiServiceTestLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("./artifact"),  # or "./" if code is in repo root
        )
