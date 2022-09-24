from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct


class SecretsStack(Stack):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Secret values required by the app which are store in the Secrets Manager
        # This values will be injected as env vars on runtime
        self.app_secrets = {
        }
