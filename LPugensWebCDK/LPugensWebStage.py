from aws_cdk import (
    Stage,
    aws_dynamodb as dynamo,
)
from constructs import Construct

from LPugensWebCDK.DBStack import DBStack
from LPugensWebCDK.DjangoAppStack import DjangoAppStack
from LPugensWebCDK.NetworkStack import NetworkStack
from LPugensWebCDK.SecretsStack import SecretsStack
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
        aws_env = kwargs.get("env")

        self.secrets = SecretsStack(self, 'secrets-stack', env=aws_env)

        self.network = NetworkStack(self, 'network-stack', env=aws_env)

        self.database = DBStack(self, f'{self.stage_name}-db-stack', self.network.vpc, stage_config, env=aws_env)

        self.django_app = DjangoAppStack(self, 'django-stack', self.network.vpc, stage_config, self.secrets.app_secrets, env=aws_env)

