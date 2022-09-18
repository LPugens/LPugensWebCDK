from aws_cdk import (
    Stage,
    aws_dynamodb as dynamo,
)
from constructs import Construct

from LPugensWebCDK.DBStack import DBStack
from LPugensWebCDK.NetworkStack import NetworkStack
from LPugensWebCDK.StageConfigs import StageConfig


class LPugensWebStage(Stage):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        stage_config: StageConfig,
        **kwargs
    ):
        super().__init__(scope, construct_id, **kwargs)

        self.network = NetworkStack(self, 'network-stack')

        self.database = DBStack(self, 'db-stack', self.network.vpc, stage_config)
