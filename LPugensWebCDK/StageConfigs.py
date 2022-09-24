from dataclasses import dataclass

from aws_cdk import Duration
from aws_cdk.aws_rds import ServerlessScalingOptions, AuroraCapacityUnit


@dataclass
class LoadBalancerConfigs:
    cpu: int
    memory_limit_mib: int
    desired_count: int
    environment: dict[str, str]


@dataclass
class StageConfig:
    aurora_scaling: ServerlessScalingOptions
    load_balancer_configs: LoadBalancerConfigs


stage_configs = {
    'dev': StageConfig(
        aurora_scaling=ServerlessScalingOptions(
            auto_pause=Duration.minutes(5),
            max_capacity=AuroraCapacityUnit.ACU_2,
        ),
        load_balancer_configs=LoadBalancerConfigs(
            cpu=1,
            memory_limit_mib=128,
            desired_count=1,
            environment={}
        )
    )
}
