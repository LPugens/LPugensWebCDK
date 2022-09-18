from dataclasses import dataclass

from aws_cdk import Duration
from aws_cdk.aws_rds import ServerlessScalingOptions


@dataclass
class StageConfig:
    aurora_scaling: ServerlessScalingOptions


stage_configs = {
    'dev': StageConfig(
        aurora_scaling=ServerlessScalingOptions(
            auto_pause=Duration.minutes(5),
        )
    )
}
