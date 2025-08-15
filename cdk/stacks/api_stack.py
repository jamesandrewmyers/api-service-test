from constructs import Construct
from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
)

class ApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        fn = _lambda.Function(self, "Handler",
            function_name="api-service-test",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",   # file.function (no .py)
            code=_lambda.Code.from_asset("../"),        # package repo root so lambda_function.py is included
            timeout=Duration.seconds(10),
            memory_size=512
        )
