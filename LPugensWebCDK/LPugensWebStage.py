from aws_cdk import (
    Stage,
    aws_dynamodb as dynamo,
)
from constructs import Construct

from LPugensWebCDK.DBStack import DBStack

class LPugensWebStage(Stage):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs
    ):
        super().__init__(scope, construct_id, **kwargs)

        self.database = DBStack(self, 'db-stack')