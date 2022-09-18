from dataclasses import dataclass

from aws_cdk import Duration
from aws_cdk.aws_rds import ServerlessScalingOptions, AuroraCapacityUnit


@dataclass
class StageConfig:
    aurora_scaling: ServerlessScalingOptions


stage_configs = {
    'dev': StageConfig(
        aurora_scaling=ServerlessScalingOptions(
            auto_pause=Duration.minutes(5),
            max_capacity=AuroraCapacityUnit.ACU_1,
        )
    )
}
