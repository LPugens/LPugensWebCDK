from aws_cdk import (
    pipelines,
    Stack,
    aws_secretsmanager as secrets,
    aws_ssm as ssm,
)
from constructs import Construct

from LPugensWebCDK.LPugensWebStage import LPugensWebStage
from LPugensWebCDK.StageConfigs import stage_configs


class LPugensWebPipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.project_name = 'LPugensWeb'
        aws_env = kwargs.get("env")

        pipeline = pipelines.CodePipeline(
            self, construct_id,
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection(
                    repo_string='LPugens/LPugensWebCDK',
                    branch='main',
                    connection_arn=ssm.StringParameter.value_for_string_parameter(
                        self, '/Github/Connection',
                    ),
                ),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",
                    # Instructs Codebuild to install required packages
                    "npx cdk synth",
                ],
            )
        )

        for stage, stage_config in stage_configs.items():
            pipeline.add_stage(LPugensWebStage(self, f'{stage}-{self.project_name}', stage_config, env=aws_env))
