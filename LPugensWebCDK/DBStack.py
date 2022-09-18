from aws_cdk import (
    aws_dynamodb as dynamo,
    Stack,
)
from constructs import Construct

class DBStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.table = dynamo.Table(
            self,
            'test_db',
            partition_key=dynamo.Attribute(
                name='id',
                type=dynamo.AttributeType.STRING,
            ),
            billing_mode=dynamo.BillingMode.PAY_PER_REQUEST,
        )